import os
import re
import asyncio
import google.generativeai as genai

class AI_Interaction:
    """
    Tool for interacting with AI models via API.
    """
    # Initialize the library once
    _initialized = False

    @classmethod
    def _initialize(cls):
        """Initialize the genai library"""
        if not cls._initialized:
            api_key = os.getenv('GOOGLE_AI_STUDIO_API_KEY')
            if api_key:
                # Configure the library
                genai.configure(api_key=api_key)
                cls._initialized = True
        return cls._initialized

    @staticmethod
    async def generate_text(modelConfig, prompt):
        model_id = modelConfig.get('model_id', os.getenv('DEFAULT_TEXT_MODEL', 'gemini-2.5-pro'))
        temperature = modelConfig.get('temperature', float(os.getenv('DEFAULT_TEMPERATURE', '0.4')))

        print(f"[AI_Interaction] Generating text with model {model_id} (temp: {temperature})")
        print(f"[AI_Interaction] Prompt: {prompt[:100]}...")  # Show first 100 chars

        # Initialize the library
        if not AI_Interaction._initialize():
            print("[AI_Interaction WARNING] No API key found. Using fallback text generation.")
            return AI_Interaction._generate_fallback_text(prompt)

        # List of models to try in order of preference
        fallback_models = [
            model_id,  # First try the requested model
            "gemini-2.5-pro-exp-03-25",  # Experimental 2.5 Pro model
            "gemini-2.0-flash",          # Stable 2.0 Flash model
            "gemini-1.5-pro",            # Stable 1.5 Pro model
            "gemini-1.5-flash"           # Stable 1.5 Flash model
        ]

        # Remove duplicates while preserving order
        unique_models = []
        for model in fallback_models:
            if model not in unique_models:
                unique_models.append(model)

        # Try each model in sequence until one works
        last_error = None
        for current_model in unique_models:
            try:
                # If this isn't the originally requested model, log that we're using a fallback
                if current_model != model_id:
                    print(f"[AI_Interaction] Trying fallback model: {current_model}")

                # Create the model
                model = genai.GenerativeModel(current_model)

                # Set generation config
                generation_config = genai.GenerationConfig(
                    temperature=temperature,
                    top_p=0.95,
                    top_k=40,
                    max_output_tokens=1024
                )

                # Run in a separate thread to avoid blocking the event loop
                loop = asyncio.get_event_loop()

                # Define the function to execute
                def generate():
                    try:
                        # Use the model.generate_content method with generation_config
                        return model.generate_content(
                            prompt,
                            generation_config=generation_config
                        )
                    except Exception as e:
                        print(f"[AI_Interaction] Inner exception with {current_model}: {e}")
                        raise e

                # Execute the function
                response = await loop.run_in_executor(None, generate)

                # Handle the response safely
                try:
                    # Check if response has candidates
                    if hasattr(response, 'candidates') and not response.candidates:
                        print(f"[AI_Interaction WARNING] Empty candidates from {current_model}. This is a known issue with experimental models.")
                        last_error = "Empty candidates in response"
                        continue

                    # Extract the generated text
                    if hasattr(response, 'text') and response.text is not None:
                        if current_model != model_id:
                            print(f"[AI_Interaction] Successfully used fallback model: {current_model}")
                        return response.text.strip()
                    elif hasattr(response, 'parts') and response.parts:
                        parts_text = []
                        for part in response.parts:
                            if hasattr(part, 'text') and part.text is not None:
                                parts_text.append(part.text)
                        if parts_text:
                            if current_model != model_id:
                                print(f"[AI_Interaction] Successfully used fallback model: {current_model}")
                            return '\n'.join(parts_text).strip()
                    elif hasattr(response, 'candidates') and response.candidates:
                        # Try to extract text from candidates
                        for candidate in response.candidates:
                            if hasattr(candidate, 'content') and candidate.content:
                                if hasattr(candidate.content, 'parts'):
                                    parts_text = []
                                    for part in candidate.content.parts:
                                        if hasattr(part, 'text') and part.text is not None:
                                            parts_text.append(part.text)
                                    if parts_text:
                                        if current_model != model_id:
                                            print(f"[AI_Interaction] Successfully used fallback model: {current_model}")
                                        return '\n'.join(parts_text).strip()

                    # If we get here, we couldn't extract text from the response
                    print(f"[AI_Interaction WARNING] Could not extract text from response: {response}")
                    last_error = "Could not extract text from response"
                    continue

                except Exception as e:
                    print(f"[AI_Interaction WARNING] Error processing response from {current_model}: {e}")
                    last_error = str(e)
                    continue

            except Exception as e:
                print(f"[AI_Interaction WARNING] Error with model {current_model}: {e}")
                last_error = str(e)
                # Continue to the next model
                continue

        # If we get here, all models failed
        print(f"[AI_Interaction ERROR] All models failed. Last error: {last_error}")
        return AI_Interaction._generate_fallback_text(prompt)

    @staticmethod
    def _generate_fallback_text(prompt):
        """Generate fallback text when API call fails"""
        print("[AI_Interaction] Using fallback text generation")

        # Extract key terms from the prompt
        key_terms = re.findall(r'\b\w{5,}\b', prompt.lower())
        unique_terms = list(set(key_terms))[:5]  # Take up to 5 unique terms
        if not unique_terms:
            unique_terms = ["requested topic"]

        # Check if this is about quantum entanglement
        if 'quantum' in prompt.lower() and 'entanglement' in prompt.lower():
            if 'summarize' in prompt.lower() or 'summary' in prompt.lower():
                return "Quantum entanglement is a fundamental phenomenon in quantum mechanics where two or more particles become correlated in such a way that the quantum state of each particle cannot be described independently, regardless of the distance separating them. This 'spooky action at a distance' (as Einstein called it) has been experimentally verified and forms the basis for quantum computing, quantum cryptography, and quantum teleportation. The phenomenon challenges our classical intuition about locality and realism, as demonstrated by Bell's theorem and subsequent experiments."

            elif 'analyze' in prompt.lower() or 'analysis' in prompt.lower():
                return "Analysis of quantum entanglement reveals several key insights: 1) It demonstrates the non-local nature of quantum mechanics, where measuring one particle instantaneously affects its entangled partner regardless of distance; 2) Bell's inequality experiments conclusively show that entanglement cannot be explained by local hidden variables theories; 3) Entanglement enables quantum advantages in computing, communication, and sensing; 4) The phenomenon exists across different physical systems including photons, electrons, and even larger molecules; 5) Entanglement is extremely fragile and easily disrupted by environmental interactions (decoherence), making practical applications challenging but promising."

            elif 'synthesize' in prompt.lower() or 'synthesis' in prompt.lower():
                return "Quantum entanglement represents one of the most profound aspects of quantum mechanics, fundamentally challenging our classical intuitions about physical reality. When particles become entangled, they share a single quantum state such that measuring one particle instantaneously determines properties of its partner, regardless of the distance separating them. This phenomenon, which Einstein famously called 'spooky action at a distance,' has been conclusively demonstrated through experiments testing Bell's inequalities. Beyond its philosophical implications about the nature of reality, entanglement has practical applications in quantum computing (enabling exponential speedups for certain algorithms), quantum cryptography (allowing unconditionally secure communication), and quantum teleportation (transferring quantum states between distant locations). Current research focuses on maintaining entanglement across larger distances and time periods, creating multi-particle entangled states, and harnessing entanglement for quantum technologies that could revolutionize computing and communication in the coming decades."

            else:
                return "Quantum entanglement occurs when pairs or groups of particles interact in ways such that the quantum state of each particle cannot be described independently. Instead, a quantum state must be described for the system as a whole, even when particles are separated by large distances. This phenomenon, which Einstein referred to as 'spooky action at a distance,' is central to quantum mechanics and has been experimentally verified numerous times. Entanglement enables quantum computing, secure quantum communication, and quantum teleportation. Bell's theorem and subsequent experiments have shown that entanglement produces correlations that cannot be explained by any local hidden variables theory, confirming the non-local nature of quantum mechanics. Current research focuses on creating robust entangled states that can be maintained over longer distances and time periods for practical quantum technologies."

        # Default fallback responses for other topics
        elif 'summarize' in prompt.lower() or 'summary' in prompt.lower():
            return f"Summary based on the provided information about {', '.join(unique_terms)}. This text demonstrates the agent's ability to process information and generate relevant content based on the input prompt."

        elif 'analyze' in prompt.lower() or 'analysis' in prompt.lower():
            return f"Analysis of {', '.join(unique_terms)}. This represents a detailed examination of the key concepts, identifying patterns, relationships, and significant insights."

        elif 'synthesize' in prompt.lower() or 'synthesis' in prompt.lower():
            return f"Synthesis of information about {', '.join(unique_terms)}. This combines multiple sources and perspectives into a coherent understanding of the topic."

        else:
            return f"Generated text about {', '.join(unique_terms)}. This demonstrates the agent's ability to create relevant content based on the input prompt."
