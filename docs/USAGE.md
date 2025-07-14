version: 0.7.0  # Reflects self version

description: "An AI Agent that assists in creating and refining prompt files, including language specifications and parameterized agent templates."

defaultTextModel:
model_id: "gemini-1.5-pro"
temperature: 0.6
defaultCodeModel:
model_id: "gemini-code"
temperature: 0.4
defaultSpecModel:
model_id: "gemini-1.5-pro"
temperature: 0.5
tags:

agent

prompt-engineering

meta

automation

code-generation

template

specification

prompt-prompt

prompt-prompt is a toolkit for defining and running .prompt agents—specialized AI-driven prompt engineering tools. It includes:

PromptEngineerAgent: Generate language specifications and agent template files.

Utility scripts for converting and activating prompts.

Installation

pip install .

Usage

PromptEngineerAgent

Import and run the agent from the promptengineer package:

from promptengineer.agent import PromptEngineerAgent
import asyncio

async def main():
    # Spec generation example
    agent = PromptEngineerAgent(
        task_description="Generate technical specification for prompt language v0.7.0",
        generation_mode="SPECIFICATION",
        target_filename="prompt_spec_v0_7_0.md"
    )
    result = await agent.run()
    print(result)

    # Template generation example
    agent = PromptEngineerAgent(
        task_description="Create template 'DataAnalysisAgent'",
        generation_mode="AGENT_TEMPLATE",
        agent_name_param="DataAnalysisAgent"
    )
    result = await agent.run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())

Scripts

Use the provided CLI entrypoint to run agents directly:

# Specification mode
scripts/engineer_agent.py SPECIFICATION --file prompt_spec_v0_7_0.md

# Template mode
scripts/engineer_agent.py AGENT_TEMPLATE --name DataAnalysisAgent

Contributing

Fork the repository and create a feature branch.

Add or update tests in tests/.

Submit a pull request with clear description of changes.

License

This project is licensed under the MIT License. See LICENSE for details.

Metadata

Version: 0.7.0

Models:

Text: gemini-1.5-pro (temp=0.6)

Code: gemini-code (temp=0.4)

Spec: gemini-1.5-pro (temp=0.5)

Tags: agent, prompt-engineering, meta, automation, code-generation, template, specification
