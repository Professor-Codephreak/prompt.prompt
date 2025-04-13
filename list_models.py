import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv(dotenv_path=Path("config/.env"))

def main():
    print("Listing all available models in Google Generative AI...")
    
    # Get API key
    api_key = os.getenv('GOOGLE_AI_STUDIO_API_KEY')
    if not api_key or api_key == 'your_api_key_here':
        print("No valid API key found in config/.env file.")
        return
    
    # Configure the client
    genai.configure(api_key=api_key)
    
    try:
        # List all models
        print("\nAvailable models:")
        models = genai.list_models()
        
        # Group models by type
        gemini_models = []
        embedding_models = []
        other_models = []
        
        for model in models:
            model_name = model.name.split('/')[-1]
            supported_methods = model.supported_generation_methods
            
            if model_name.startswith('gemini-'):
                gemini_models.append((model_name, supported_methods))
            elif 'embedding' in model_name:
                embedding_models.append((model_name, supported_methods))
            else:
                other_models.append((model_name, supported_methods))
        
        # Print Gemini models
        if gemini_models:
            print("\nGemini Models:")
            for model_name, methods in gemini_models:
                print(f"  - {model_name}")
                print(f"    Supported methods: {', '.join(methods)}")
        
        # Print Embedding models
        if embedding_models:
            print("\nEmbedding Models:")
            for model_name, methods in embedding_models:
                print(f"  - {model_name}")
                print(f"    Supported methods: {', '.join(methods)}")
        
        # Print Other models
        if other_models:
            print("\nOther Models:")
            for model_name, methods in other_models:
                print(f"  - {model_name}")
                print(f"    Supported methods: {', '.join(methods)}")
        
        print("\nTotal models available:", len(models))
        
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    main()
