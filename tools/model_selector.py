import os
import google.generativeai as genai
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=Path("config/.env"))

class ModelSelector:
    """
    Tool for selecting and managing AI models.
    """

    # Model categories
    CATEGORIES = {
        "Latest Models": [
            "gemini-2.5-pro-exp-03-25",
            "gemini-2.0-pro-exp",
            "gemini-2.0-flash",
        ],
        "Balanced Models": [
            "gemini-1.5-pro",
            "gemini-1.5-flash",
        ],
        "Legacy Models": [
            "gemini-1.0-pro-vision-latest",
        ]
    }

    # Model descriptions
    MODEL_INFO = {
        "gemini-2.5-pro-exp-03-25": {
            "description": "Latest experimental Gemini 2.5 Pro model with advanced reasoning (EXPERIMENTAL)",
            "strengths": "Complex reasoning, creative content, detailed responses",
            "use_cases": "Research, content creation, complex problem-solving",
            "token_limit": 1048576,  # 1M tokens
            "multimodal": True,
            "experimental": True,
            "note": "This is an experimental model and has known issues with empty responses. The system will automatically fall back to a stable model when these issues occur. You may see warnings about 'empty candidates' or 'NoneType' errors."
        },
        "gemini-2.0-pro-exp": {
            "description": "Experimental Gemini 2.0 Pro with strong reasoning capabilities",
            "strengths": "Reasoning, instruction following, content generation",
            "use_cases": "General purpose AI tasks, content creation",
            "token_limit": 524288,  # 512K tokens
            "multimodal": True
        },
        "gemini-2.0-flash": {
            "description": "Fast Gemini 2.0 model with good balance of speed and quality",
            "strengths": "Speed, efficiency, good reasoning capabilities",
            "use_cases": "Interactive applications, quick responses, general tasks",
            "token_limit": 524288,  # 512K tokens
            "multimodal": True
        },
        "gemini-1.5-pro": {
            "description": "Versatile model with good balance of capabilities",
            "strengths": "Long context understanding, code generation, summarization",
            "use_cases": "Programming assistance, document analysis",
            "token_limit": 1048576,  # 1M tokens
            "multimodal": True
        },
        "gemini-1.5-flash": {
            "description": "Fast and efficient model for quicker responses",
            "strengths": "Speed, efficiency, good for interactive use",
            "use_cases": "Chat applications, quick responses, basic tasks",
            "token_limit": 1048576,  # 1M tokens
            "multimodal": True
        },
        "gemini-1.0-pro": {
            "description": "First generation Gemini model",
            "strengths": "General text generation and understanding",
            "use_cases": "Basic text generation and understanding",
            "token_limit": 32768,  # 32K tokens
            "multimodal": False
        },
        "gemini-1.0-pro-vision": {
            "description": "First generation Gemini model with vision capabilities",
            "strengths": "Image understanding and analysis",
            "use_cases": "Image captioning, visual question answering",
            "token_limit": 16384,  # 16K tokens
            "multimodal": True
        }
    }

    @classmethod
    def get_available_models(cls):
        """Get list of available models from the API"""
        try:
            # Configure the client
            api_key = os.getenv('GOOGLE_AI_STUDIO_API_KEY')
            if not api_key or api_key == 'your_api_key_here':
                print("[ModelSelector WARNING] No API key found or using placeholder. Using predefined model list.")
                return cls._get_predefined_models()

            # Initialize the API
            genai.configure(api_key=api_key)

            # Get models from API
            models = genai.list_models()

            # Filter for text generation models
            available_models = []
            for model in models:
                model_name = model.name.split('/')[-1]
                if model_name.startswith('gemini-'):
                    available_models.append(model_name)

            # If no models found, use predefined list
            if not available_models:
                print("[ModelSelector WARNING] No models found from API. Using predefined model list.")
                return cls._get_predefined_models()

            return available_models
        except Exception as e:
            print(f"[ModelSelector ERROR] Error fetching models: {e}")
            return cls._get_predefined_models()

    @classmethod
    def _get_predefined_models(cls):
        """Get predefined list of models"""
        # Always include these models regardless of API availability
        must_include = ["gemini-2.5-pro-exp-03-25", "gemini-1.5-pro"]

        # Get all models from categories
        models = []
        for category in cls.CATEGORIES.values():
            models.extend(category)

        # Make sure must-include models are in the list
        for model in must_include:
            if model not in models:
                models.append(model)

        return models

    @classmethod
    def display_model_selection(cls):
        """Display model selection interface"""
        print("\n===== AI Model Selection =====")

        # Get available models
        available_models = cls.get_available_models()

        # Always include these models in the display
        must_display = ["gemini-2.5-pro", "gemini-1.5-pro"]
        for model in must_display:
            if model not in available_models:
                available_models.append(model)

        # Display models by category
        model_options = []
        option_num = 1

        for category_name, category_models in cls.CATEGORIES.items():
            # Check if any models in this category are available
            category_has_models = any(model in available_models for model in category_models)

            if category_has_models:
                print(f"\n{category_name}:")

                for model in category_models:
                    if model in available_models:
                        model_info = cls.MODEL_INFO.get(model, {"description": "No description available"})
                        print(f"  {option_num}. {model}")
                        print(f"     {model_info['description']}")
                        model_options.append(model)
                        option_num += 1

        # If no models are available, use default
        if not model_options:
            default_model = os.getenv('DEFAULT_TEXT_MODEL', 'gemini-2.5-pro')
            print(f"\nNo models available. Using default model: {default_model}")
            return default_model

        # Get user selection
        try:
            selection = input("\nSelect a model (number) or press Enter for default: ")

            if selection.strip() == "":
                # Use default model
                selected_model = os.getenv('DEFAULT_TEXT_MODEL', 'gemini-2.5-pro')
                print(f"Using default model: {selected_model}")
                return selected_model

            selection_idx = int(selection) - 1
            if 0 <= selection_idx < len(model_options):
                selected_model = model_options[selection_idx]
                print(f"Selected model: {selected_model}")

                # Display detailed information
                if selected_model in cls.MODEL_INFO:
                    info = cls.MODEL_INFO[selected_model]
                    print(f"\nModel: {selected_model}")
                    print(f"Description: {info['description']}")
                    print(f"Strengths: {info['strengths']}")
                    print(f"Use Cases: {info['use_cases']}")
                    print(f"Token Limit: {info['token_limit']}")
                    print(f"Multimodal: {'Yes' if info['multimodal'] else 'No'}")

                    # Show experimental note if applicable
                    if info.get('experimental', False):
                        print(f"\nNOTE: {info.get('note', 'This is an experimental model.')}")

                return selected_model
            else:
                print("Invalid selection. Using default model.")
                selected_model = os.getenv('DEFAULT_TEXT_MODEL', 'gemini-2.5-pro')
                print(f"Using default model: {selected_model}")
                return selected_model
        except (ValueError, EOFError):
            # Handle errors by using default model
            selected_model = os.getenv('DEFAULT_TEXT_MODEL', 'gemini-2.5-pro')
            print(f"Error in selection. Using default model: {selected_model}")
            return selected_model

    @classmethod
    def create_model_config(cls, model_name=None, temperature=None):
        """Create a model configuration dictionary"""
        if model_name is None:
            model_name = os.getenv('DEFAULT_TEXT_MODEL', 'gemini-2.5-pro')

        if temperature is None:
            temperature = float(os.getenv('DEFAULT_TEMPERATURE', '0.4'))

        return {
            "model_id": model_name,
            "temperature": temperature
        }


if __name__ == "__main__":
    # Test the model selector
    print("Testing Model Selector...")
    selected_model = ModelSelector.display_model_selection()
    print(f"Final selected model: {selected_model}")

    # Create model config
    config = ModelSelector.create_model_config(selected_model)
    print(f"Model config: {config}")
