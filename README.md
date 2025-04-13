# BDI Agent with Real Tools

This project implements a BDI (Belief-Desire-Intention) agent architecture that uses real tools to interact with the environment. The agent can perform web searches, take notes, and use AI models for text generation.

## Project Structure

```
.
├── config/           # Configuration files
│   ├── .env          # Environment variables (API keys)
│   └── metadata.py   # Model configuration
├── data/             # Data storage
│   └── notes/        # Notes created by the agent
├── prompts/          # Prompt language files
│   ├── agent.prompt  # Research assistant agent
│   ├── bdi_agent.prompt # BDI agent implementation
│   └── rules.prompt  # Language rules
├── scripts/          # Python scripts
│   └── bdi_agent.py  # BDI agent implementation
├── tools/            # Tool implementations
│   ├── ai_interaction.py # AI model interaction
│   ├── note_taking.py    # Note-taking tool
│   ├── summarization.py  # Text summarization
│   └── web_search.py     # Web search tool
├── main.py           # Main entry point
└── requirements.txt  # Dependencies
```

## Features

- **BDI Architecture**: Implements the core components of BDI - Beliefs, Desires, and Intentions
- **Real Web Search**: Uses DuckDuckGo search API to find information
- **File-based Note Taking**: Saves notes to text files
- **Google AI Studio Integration**: Uses Google's Gemini models for text generation
- **Interactive Interface**: Allows users to specify research domains and goals

## Setup

1. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

2. **Set up Google AI Studio API key**:
   - Edit the `config/.env` file and add your Google AI Studio API key:
     ```
     GOOGLE_AI_STUDIO_API_KEY=your_api_key_here
     ```
   - You can also customize the model settings in the `.env` file

3. **Run the agent**:
   ```
   python main.py
   ```

## How It Works

The BDI agent follows the perceive-deliberate-plan-execute cycle:

1. **Perceive**: The agent observes the environment and updates its beliefs
2. **Deliberate**: The agent considers its desires and determines goals
3. **Plan**: The agent creates a plan to achieve the selected goal
4. **Execute**: The agent carries out the current intention

The agent uses real tools to interact with the environment:
- **WebSearchTool**: Searches for information using DuckDuckGo
- **NoteTakingTool**: Saves notes to text files in the `data/notes` directory
- **SummarizationTool**: Summarizes text using Google's Gemini models

## Example Usage

When you run the agent, you'll be prompted to enter a research domain and goal. The agent will then:

1. Search for information about the domain
2. Take notes on the findings
3. Summarize the information
4. Analyze the information
5. Synthesize a comprehensive overview

The final output and all notes will be saved to the `data/notes` directory.

## Customization

You can customize the agent's behavior by modifying the `config/.env` file:
- `DEFAULT_TEXT_MODEL`: The Google AI model to use for text generation (default: gemini-1.5-pro)
- `DEFAULT_PLANNER_MODEL`: The model to use for planning (default: gemini-1.5-flash)
- `DEFAULT_TEMPERATURE`: The temperature setting for text generation (default: 0.4)
