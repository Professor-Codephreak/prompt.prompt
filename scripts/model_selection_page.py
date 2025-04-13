import os
from tools.model_selector import ModelSelector

class ModelSelectionPage:
    """
    Interactive page for selecting AI models and configuring parameters.
    """

    @staticmethod
    def display_header():
        """Display the header of the model selection page"""
        print("\n" + "=" * 60)
        print("  BDI AGENT - MODEL SELECTION")
        print("=" * 60)
        print("\nSelect the AI model you want to use for this session.")
        print("Different models have different capabilities and performance characteristics.")
        print("\nNote: Gemini 2.5 Pro Experimental (gemini-2.5-pro-exp-03-25) is available")
        print("and will be used as the default model. This experimental model has known issues")
        print("with empty responses and 'NoneType' errors. If these issues occur, the system")
        print("will automatically fall back to a stable model like Gemini 1.5 Pro.")

    @staticmethod
    def display_temperature_selection():
        """Display temperature selection interface"""
        print("\n----- Temperature Setting -----")
        print("Temperature controls the randomness of the model's output.")
        print("Lower values (0.0-0.3): More focused, deterministic, and factual")
        print("Medium values (0.3-0.7): Balanced creativity and coherence")
        print("Higher values (0.7-1.0): More creative, diverse, and unexpected")

        try:
            default_temp = os.getenv('DEFAULT_TEMPERATURE', '0.4')
            temp_input = input(f"\nSelect temperature (0.0-1.0) or press Enter for default ({default_temp}): ")

            if temp_input.strip() == "":
                # Use default temperature
                temperature = float(default_temp)
                print(f"Using default temperature: {temperature}")
                return temperature

            temperature = float(temp_input)
            if 0.0 <= temperature <= 1.0:
                print(f"Selected temperature: {temperature}")
                return temperature
            else:
                print("Temperature must be between 0.0 and 1.0. Using default.")
                temperature = float(default_temp)
                print(f"Using default temperature: {temperature}")
                return temperature
        except (ValueError, EOFError):
            # Handle errors by using default temperature
            temperature = float(default_temp)
            print(f"Error in selection. Using default temperature: {temperature}")
            return temperature

    @staticmethod
    def run():
        """Run the model selection page"""
        ModelSelectionPage.display_header()

        # Select model
        selected_model = ModelSelector.display_model_selection()

        # Select temperature
        temperature = ModelSelectionPage.display_temperature_selection()

        # Create and return model configuration
        model_config = {
            "model_id": selected_model,
            "temperature": temperature
        }

        print("\nModel configuration complete!")
        print(f"Model: {model_config['model_id']}")
        print(f"Temperature: {model_config['temperature']}")
        print("=" * 60 + "\n")

        return model_config


if __name__ == "__main__":
    # Test the model selection page
    config = ModelSelectionPage.run()
    print(f"Final configuration: {config}")
