import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Metadata:
    """
    Configuration metadata for the BDI agent.
    """
    def __init__(self):
        # Load model configuration from environment variables or use defaults
        self.defaultTextModel = {
            "model_id": os.getenv('DEFAULT_TEXT_MODEL', 'gemini-1.5-pro'),
            "temperature": float(os.getenv('DEFAULT_TEMPERATURE', '0.4'))
        }
        self.defaultPlannerModel = {
            "model_id": os.getenv('DEFAULT_PLANNER_MODEL', 'gemini-1.5-flash'),
            "temperature": float(os.getenv('DEFAULT_PLANNER_TEMPERATURE', '0.7'))
        }

# Create a singleton instance
metadata = Metadata()
