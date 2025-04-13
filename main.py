import os
import asyncio
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path=Path("config/.env"))

# Import the BDI agent and model selection page
from scripts.bdi_agent import BDIAgent
from scripts.model_selection_page import ModelSelectionPage
from config.metadata import metadata

async def main():
    print("[SCRIPT START] BDI Agent Architecture Demo")

    # Check if API key is configured
    api_key = os.getenv('GOOGLE_AI_STUDIO_API_KEY')
    if not api_key or api_key == 'your_api_key_here':
        print("\n[WARNING] No Google AI Studio API key found in config/.env file.")
        print("The agent will use fallback text generation instead of the actual API.")
        print("To use the Google AI Studio API, edit the config/.env file with your API key.")
        print("You can copy the config/.env.template file to config/.env and add your API key.\n")

    # Run model selection page
    print("\nBefore we begin, let's select the AI model to use for this session.")
    model_config = ModelSelectionPage.run()

    # Update metadata with selected model
    metadata.defaultTextModel = model_config

    # Define domain and goal
    domain = input("Enter a research domain (default: artificial intelligence ethics): ").strip() or "artificial intelligence ethics"
    goal = input("Enter a research goal (default: Research key principles and provide overview): ").strip() or "Research key principles and provide comprehensive overview"

    print(f"\nInitializing BDI agent with domain: '{domain}' and goal: '{goal}'")
    print(f"Using AI model: {model_config['model_id']} (temperature: {model_config['temperature']})")

    # Instantiate BDI agent
    bdi_agent = BDIAgent(domain=domain, initial_goal=goal)

    # Run agent BDI cycle
    max_cycles = 8
    print(f"Running agent for maximum {max_cycles} cycles...\n")
    final_result = await bdi_agent.run(max_cycles=max_cycles)

    print("\n--- Agent Final Output ---")
    print(final_result)
    print("--------------------------")

    # Show where notes are stored
    notes_dir = Path("data/notes")
    if notes_dir.exists() and any(notes_dir.iterdir()):
        print(f"\nNotes have been saved to the '{notes_dir}' directory.")
        print("Files created:")
        for file in notes_dir.iterdir():
            if file.is_file():
                print(f"  - {file.name}")

    print("[SCRIPT END]")

if __name__ == "__main__":
    asyncio.run(main())
