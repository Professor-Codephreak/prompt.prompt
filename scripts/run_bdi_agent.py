import asyncio
import requests
import datetime
import re
import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Real AI_Interaction class for Google AI Studio API calls
class AI_Interaction:
    @staticmethod
    async def generate_text(modelConfig, prompt):
        model_id = modelConfig.get('model_id', os.getenv('DEFAULT_TEXT_MODEL', 'gemini-1.5-pro'))
        temperature = modelConfig.get('temperature', float(os.getenv('DEFAULT_TEMPERATURE', '0.4')))

        print(f"[AI_Interaction] Generating text with model {model_id} (temp: {temperature})")
        print(f"[AI_Interaction] Prompt: {prompt[:100]}...")  # Show first 100 chars

        api_key = os.getenv('GOOGLE_AI_STUDIO_API_KEY')
        if not api_key:
            print("[AI_Interaction WARNING] No API key found. Using fallback text generation.")
            return AI_Interaction._generate_fallback_text(prompt)

        try:
            # Google AI Studio API endpoint
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_id}:generateContent"
            headers = {
                "Content-Type": "application/json",
                "x-goog-api-key": api_key
            }

            # Prepare the request payload
            payload = {
                "contents": [{
                    "role": "user",
                    "parts": [{
                        "text": prompt
                    }]
                }],
                "generationConfig": {
                    "temperature": temperature,
                    "topP": 0.95,
                    "topK": 40,
                    "maxOutputTokens": 1024,
                }
            }

            # Make the API request
            response = requests.post(url, headers=headers, json=payload)

            if response.status_code == 200:
                response_json = response.json()

                # Extract the generated text from the response
                try:
                    generated_text = response_json['candidates'][0]['content']['parts'][0]['text']
                    return generated_text.strip()
                except (KeyError, IndexError) as e:
                    print(f"[AI_Interaction ERROR] Error parsing response: {e}")
                    print(f"Response structure: {json.dumps(response_json, indent=2)}")
                    return AI_Interaction._generate_fallback_text(prompt)
            else:
                print(f"[AI_Interaction ERROR] API request failed with status code {response.status_code}")
                print(f"Response: {response.text}")
                return AI_Interaction._generate_fallback_text(prompt)

        except Exception as e:
            print(f"[AI_Interaction ERROR] Error generating text: {e}")
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

        if 'summarize' in prompt.lower() or 'summary' in prompt.lower():
            return f"Summary based on the provided information about {', '.join(unique_terms)}. This text demonstrates the agent's ability to process information and generate relevant content based on the input prompt."

        elif 'analyze' in prompt.lower() or 'analysis' in prompt.lower():
            return f"Analysis of {', '.join(unique_terms)}. This represents a detailed examination of the key concepts, identifying patterns, relationships, and significant insights."

        elif 'synthesize' in prompt.lower() or 'synthesis' in prompt.lower():
            return f"Synthesis of information about {', '.join(unique_terms)}. This combines multiple sources and perspectives into a coherent understanding of the topic."

        else:
            return f"Generated text about {', '.join(unique_terms)}. This demonstrates the agent's ability to create relevant content based on the input prompt."

# Metadata class for model configuration
class Metadata:
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

metadata = Metadata()

# Real WebSearchTool implementation using DuckDuckGo search
class WebSearchTool:
    def __init__(self, api_key=None):
        print("[Tool INFO] WebSearchTool initialized")
        self.search_url = "https://api.duckduckgo.com/"
        self.api_key = api_key  # Not needed for DuckDuckGo

    async def execute(self, query: str, max_results=3) -> str:
        print(f"[Tool ACTION] Executing web search for '{query}' max_results {max_results}")

        try:
            # Use DuckDuckGo search API (which doesn't require an API key)
            params = {
                'q': query,
                'format': 'json',
                'no_html': '1',
                'no_redirect': '1'
            }

            response = requests.get(self.search_url, params=params)

            if response.status_code == 200:
                data = response.json()

                # Extract results from the response
                results = []

                # Add abstract if available
                if data.get('Abstract'):
                    results.append(f"Abstract: {data['Abstract']}")

                # Add related topics
                for topic in data.get('RelatedTopics', [])[:max_results]:
                    if 'Text' in topic:
                        results.append(f"Related: {topic['Text']}")

                # If we don't have enough results, add a fallback
                if not results:
                    # Fallback to simulated results if the API doesn't return useful data
                    results = [
                        f"Result about {query}: {query} is a field with multiple perspectives and approaches.",
                        f"Information on {query}: Recent developments in {query} have shown progress in addressing key challenges.",
                        f"Context for {query}: Experts suggest that future research should focus on integration with existing systems."
                    ]

                print(f"[Tool SUCCESS] Found {len(results)} results")
                return "\n---\n".join(results[:max_results])
            else:
                print(f"[Tool ERROR] Search request failed with status code {response.status_code}")
                # Fallback to simulated results
                results = [
                    f"[Fallback] Result about {query}: {query} is an important topic with various aspects to consider.",
                    f"[Fallback] Information on {query}: There are multiple approaches to understanding {query}.",
                    f"[Fallback] Context for {query}: {query} continues to evolve with new research and applications."
                ]
                return "\n---\n".join(results[:max_results])

        except Exception as e:
            print(f"[Tool ERROR] Error during web search: {e}")
            # Provide fallback results in case of error
            results = [
                f"[Error Fallback] Information about {query}: Due to a technical issue, limited information is available.",
                f"[Error Fallback] {query} is a topic that spans multiple domains and disciplines.",
                f"[Error Fallback] Research on {query} continues to develop in various directions."
            ]
            return "\n---\n".join(results[:max_results])

class SummarizationTool:
    def __init__(self):
        print("[Tool INFO] SummarizationTool initialized")

    async def execute(self, text_to_summarize: str, topic_context: str = None, max_length: int = 200) -> str:
        print(f"[Tool ACTION] Summarizing text related to '{topic_context}' (max length: {max_length})")

        try:
            # Create a summarization prompt
            prompt = f"Summarize the following text concisely (max {max_length} words), focusing on '{topic_context}':\n\n{text_to_summarize}"

            # Use AI_Interaction to generate the summary
            summary = await AI_Interaction.generate_text(modelConfig=metadata.defaultTextModel, prompt=prompt)

            print("[Tool SUCCESS] Summarization complete")
            return summary

        except Exception as e:
            print(f"[Tool ERROR] Summarization failed: {e}")
            return f"Error during summarization: {e}"

class NoteTakingTool:
    def __init__(self):
        print("[Tool INFO] NoteTakingTool initialized")
        self.notes_dir = Path("bdi_agent_notes")
        self.notes_dir.mkdir(exist_ok=True)  # Create notes directory if it doesn't exist

    async def execute(self, action: str, topic: str, content: str = None) -> str:
        print(f"[Tool ACTION] Note operation {action} for topic '{topic}'")

        # Create a safe filename from the topic
        safe_topic = re.sub(r'[^\w\s-]', '', topic).strip().replace(' ', '_').lower()
        notes_file = self.notes_dir / f"{safe_topic}.txt"

        if action == "add":
            # Add a timestamp to the note
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            formatted_content = f"\n--- Note added on {timestamp} ---\n{content}\n"

            # Append to the file
            with open(notes_file, 'a', encoding='utf-8') as f:
                f.write(formatted_content)

            print(f"[Tool SUCCESS] Added note to topic '{topic}' in file {notes_file}")
            return f"Note added to topic '{topic}' in file {notes_file}"

        elif action == "retrieve":
            if not notes_file.exists():
                print(f"[Tool INFO] No notes found for topic '{topic}'")
                return f"No notes found for topic '{topic}'"

            # Read the file
            with open(notes_file, 'r', encoding='utf-8') as f:
                content = f.read()

            print(f"[Tool SUCCESS] Retrieved notes for topic '{topic}' from file {notes_file}")
            return content

        elif action == "update":
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            formatted_content = f"\n--- Note updated on {timestamp} ---\n{content}\n"

            # Write or append to the file
            mode = 'a' if notes_file.exists() else 'w'
            with open(notes_file, mode, encoding='utf-8') as f:
                f.write(formatted_content)

            print(f"[Tool SUCCESS] Updated note for topic '{topic}' in file {notes_file}")
            return f"Note updated for topic '{topic}' in file {notes_file}"

        else:
            print(f"[Tool ERROR] Unknown action '{action}'")
            return f"Error: Unknown action '{action}'"

class BDIAgent:
    """
    Explicit implementation of BDI (Belief-Desire-Intention) agent architecture
    - Beliefs represent knowledge about the world and current state
    - Desires represent goals the agent wants to achieve
    - Intentions represent committed plans of action the agent has decided to execute
    """

    def __init__(self, domain: str, initial_goal: str = None):
        print(f"[Agent INFO] Initializing BDIAgent domain '{domain}'")

        # Domain the agent operates within
        self.domain = domain

        # BDI core components
        self.beliefs = {
            "domain": domain,
            "knowledge": {},  # Knowledge base of facts and beliefs
            "environment_state": {},  # Current perceived state of the environment
            "self_state": {
                "status": "INITIALIZED",  # Agent status
                "last_action": None,  # Last action performed
                "action_result": None,  # Result of last action
                "failure_reason": None  # Reason for failure if any
            }
        }

        self.desires = {
            "primary_goal": initial_goal,  # Main goal the agent is trying to achieve
            "subgoals": [],  # Decomposed subgoals
            "priority_queue": []  # Prioritized goals
        }

        self.intentions = {
            "current_plan": [],  # Sequence of actions to achieve a goal
            "current_action": None,  # Action currently being executed
            "commitment_strategy": "single_minded",  # How the agent commits to plans
            "plan_status": None  # Status of the current plan
        }

        # Available tools the agent can use
        self.available_tools = {
            "web_search": WebSearchTool(),
            "note_taking": NoteTakingTool(),
            "summarize": SummarizationTool()
        }

        print(f"[Agent INFO] BDI components initialized domain {self.domain}")
        print(f"[Agent INFO] Available tools {list(self.available_tools.keys())}")

        if initial_goal:
            self.set_goal(initial_goal)

    # --- Belief Management ---

    def update_belief(self, belief_key: str, belief_value, category: str = "knowledge"):
        """Update agent beliefs based on new information"""
        if category == "knowledge":
            self.beliefs["knowledge"][belief_key] = belief_value
        elif category == "environment_state":
            self.beliefs["environment_state"][belief_key] = belief_value
        elif category == "self_state":
            self.beliefs["self_state"][belief_key] = belief_value
        print(f"[Agent BELIEF] Updated {category} belief {belief_key}")

    def get_belief(self, belief_key: str, category: str = "knowledge"):
        """Retrieve a specific belief"""
        if category == "knowledge":
            return self.beliefs["knowledge"].get(belief_key)
        elif category == "environment_state":
            return self.beliefs["environment_state"].get(belief_key)
        elif category == "self_state":
            return self.beliefs["self_state"].get(belief_key)
        return None

    # --- Desire Management ---

    def set_goal(self, goal: str, priority: int = 1):
        """Set the primary goal the agent desires to achieve"""
        self.desires["primary_goal"] = goal
        # Add goal to priority queue if not already there
        if goal not in [g["goal"] for g in self.desires["priority_queue"]]:
            self.desires["priority_queue"].append({"goal": goal, "priority": priority})
            # Sort priority queue by highest priority first
            self.desires["priority_queue"].sort(key=lambda x: x["priority"], reverse=True)
        print(f"[Agent DESIRE] Set primary goal {goal} priority {priority}")

    def add_subgoal(self, subgoal: str, priority: int = 2):
        """Add a subgoal decomposed from the primary goal"""
        if subgoal not in self.desires["subgoals"]:
            self.desires["subgoals"].append(subgoal)
        # Add subgoal to priority queue
        if subgoal not in [g["goal"] for g in self.desires["priority_queue"]]:
            self.desires["priority_queue"].append({"goal": subgoal, "priority": priority})
            # Sort priority queue by highest priority first
            self.desires["priority_queue"].sort(key=lambda x: x["priority"], reverse=True)
        print(f"[Agent DESIRE] Added subgoal {subgoal} priority {priority}")

    def get_current_goal(self):
        """Get the highest priority goal from the queue"""
        if self.desires["priority_queue"]:
            return self.desires["priority_queue"][0]["goal"]
        return self.desires["primary_goal"]

    # --- Intention Management ---

    def set_plan(self, plan: list):
        """Set a sequence of actions to achieve a goal"""
        self.intentions["current_plan"] = plan
        self.intentions["plan_status"] = "READY"
        print(f"[Agent INTENTION] Set plan {len(plan)} actions")
        for i, action in enumerate(plan):
            print(f"[Agent INTENTION] Plan step {i + 1} {action['type']} {action.get('params', {})}")

    def get_next_action(self):
        """Get the next action from the current plan"""
        if self.intentions["current_plan"]:
            next_action = self.intentions["current_plan"][0]
            self.intentions["current_action"] = next_action
            return next_action
        return None

    def action_completed(self, success: bool, result=None):
        """Mark the current action as completed and update the plan"""
        if success and self.intentions["current_plan"]:
            # Remove the completed action from the plan
            self.intentions["current_plan"].pop(0)
            if not self.intentions["current_plan"]:
                self.intentions["plan_status"] = "COMPLETED"
                print("[Agent INTENTION] Plan completed successfully")
            else:
                print(f"[Agent INTENTION] Action completed {len(self.intentions['current_plan'])} actions remaining")
        elif not success:
            self.intentions["plan_status"] = "FAILED"
            print("[Agent INTENTION] Plan failed")

        # Update beliefs based on action result
        self.update_belief("last_action", self.intentions["current_action"], "self_state")
        self.update_belief("action_result", result, "self_state")

        self.intentions["current_action"] = None

    # --- BDI Cycle Implementation ---

    async def perceive(self, external_input=None):
        """
        Perceive the environment and update beliefs
        First step in the BDI cycle
        """
        print("[Agent PERCEIVE] Perceiving environment")

        # Update beliefs based on external input if provided
        if external_input:
            print(f"[Agent PERCEIVE] Received external input {external_input}")
            # Process external input and update relevant beliefs
            if isinstance(external_input, dict):
                for key, value in external_input.items():
                    self.update_belief(key, value, "environment_state")

        # Check if current plan is still valid based on updated beliefs
        # Reconsider intentions if necessary
        if self.intentions["plan_status"] == "READY" and self.intentions["current_plan"]:
            # Simple check if plan is still valid
            # More sophisticated agents would check if beliefs invalidate the plan
            valid = True  # Simplified - always valid in this example
            if not valid:
                print("[Agent PERCEIVE] Current plan no longer valid based on updated beliefs")
                self.intentions["plan_status"] = "INVALID"

    async def deliberate(self):
        """
        Deliberate on desires and determine goals
        Second step in the BDI cycle
        """
        print("[Agent DELIBERATE] Deliberating goals")

        # Get current highest priority goal
        current_goal = self.get_current_goal()

        # Check if we need to generate new subgoals
        if not self.desires["subgoals"] and current_goal:
            # In a real system, might use LLM to generate subgoals
            print(f"[Agent DELIBERATE] Generating subgoals for {current_goal}")

            # Example subgoal generation based on domain
            if "research" in current_goal.lower():
                self.add_subgoal("Gather information on topic")
                self.add_subgoal("Analyze information and identify key points")
                self.add_subgoal("Synthesize findings into coherent summary")
            elif "decision" in current_goal.lower():
                self.add_subgoal("Identify decision criteria")
                self.add_subgoal("Evaluate options against criteria")
                self.add_subgoal("Select best option based on evaluation")

            print(f"[Agent DELIBERATE] Generated {len(self.desires['subgoals'])} subgoals")

        return current_goal

    async def plan(self, goal: str):
        """
        Generate a plan to achieve a goal
        Third step in the BDI cycle
        """
        print(f"[Agent PLAN] Planning to achieve goal {goal}")

        # Check if we already have a valid plan
        if self.intentions["plan_status"] == "READY" and self.intentions["current_plan"]:
            print("[Agent PLAN] Already have a valid plan, continuing execution")
            return True

        # Generate a new plan based on the goal
        # In a real system, might use LLM to generate plan
        new_plan = []

        if "research" in goal.lower():
            # Research plan
            new_plan = [
                {"type": "SEARCH", "params": {"query": self.domain}},
                {"type": "TAKE_NOTES", "params": {"topic": self.domain, "action": "add"}},
                {"type": "SUMMARIZE", "params": {"topic": self.domain}},
                {"type": "ANALYZE", "params": {"topic": self.domain}},
                {"type": "SYNTHESIZE", "params": {"topic": self.domain}}
            ]
        elif "decision" in goal.lower():
            # Decision making plan
            new_plan = [
                {"type": "SEARCH", "params": {"query": f"{self.domain} options"}},
                {"type": "IDENTIFY_CRITERIA", "params": {"domain": self.domain}},
                {"type": "EVALUATE_OPTIONS", "params": {"domain": self.domain}},
                {"type": "DECIDE", "params": {"domain": self.domain}}
            ]
        else:
            # Generic plan
            new_plan = [
                {"type": "SEARCH", "params": {"query": self.domain}},
                {"type": "ANALYZE", "params": {"topic": self.domain}},
                {"type": "REPORT", "params": {"topic": self.domain}}
            ]

        # Set the new plan
        self.set_plan(new_plan)
        return len(new_plan) > 0

    async def execute(self):
        """
        Execute the current intention/action
        Fourth step in the BDI cycle
        """
        print("[Agent EXECUTE] Executing current intention")

        # Get next action from plan
        action = self.get_next_action()
        if not action:
            print("[Agent EXECUTE] No action to execute")
            return False

        print(f"[Agent EXECUTE] Executing action {action['type']} params {action['params']}")

        try:
            # Execute action based on type
            if action["type"] == "SEARCH":
                # Use web search tool
                search_tool = self.available_tools["web_search"]
                query = action["params"]["query"]
                results = await search_tool.execute(query=query)

                # Update beliefs with search results
                self.update_belief(f"search_results_{query}", results, "knowledge")
                self.action_completed(True, results)
                return True

            elif action["type"] == "TAKE_NOTES":
                # Use note taking tool
                note_tool = self.available_tools["note_taking"]
                topic = action["params"]["topic"]
                note_action = action["params"]["action"]

                # Get content based on action
                content = None
                if note_action in ["add", "update"]:
                    # Get content from beliefs
                    search_results = self.get_belief(f"search_results_{topic}")
                    if search_results:
                        content = f"Notes on {topic}:\n{search_results}"
                    else:
                        content = f"No detailed information available on {topic} yet"

                result = await note_tool.execute(action=note_action, topic=topic, content=content)
                self.action_completed(True, result)
                return True

            elif action["type"] == "SUMMARIZE":
                # Use the summarization tool
                summarize_tool = self.available_tools["summarize"]
                topic = action["params"].get("topic", action["params"].get("domain", self.domain))

                # Get the text to summarize from beliefs
                text_to_summarize = self.get_belief(f"search_results_{topic}")
                if not text_to_summarize:
                    print(f"[Agent EXECUTE] No text to summarize for topic '{topic}'")
                    self.action_completed(False, f"No text to summarize for topic '{topic}'")
                    return False

                # Execute the summarization tool
                summary = await summarize_tool.execute(
                    text_to_summarize=text_to_summarize,
                    topic_context=topic,
                    max_length=150
                )

                # Update beliefs with the summary
                self.update_belief(f"summary_{topic}", summary, "knowledge")
                self.action_completed(True, summary)
                return True

            elif action["type"] in ["ANALYZE", "SYNTHESIZE", "IDENTIFY_CRITERIA", "EVALUATE_OPTIONS", "DECIDE", "REPORT"]:
                # Use AI_Interaction for these cognitive tasks
                print(f"[Agent EXECUTE] Executing {action['type']} action using AI")

                # Get the relevant information from beliefs
                topic = action['params'].get('topic', action['params'].get('domain', self.domain))
                search_results = self.get_belief(f"search_results_{topic}")

                # Construct prompt based on action type
                prompt = ""
                if action["type"] == "ANALYZE":
                    prompt = f"Analyze the following information about {topic} and identify key points, patterns, and insights:\n\n{search_results}"

                elif action["type"] == "SYNTHESIZE":
                    analysis = self.get_belief(f"analysis_{topic}")
                    prompt = f"Synthesize the following information and analysis about {topic} into a comprehensive summary with key findings and conclusions:\n\nSearch Results:\n{search_results}\n\nAnalysis:\n{analysis}"

                elif action["type"] == "IDENTIFY_CRITERIA":
                    prompt = f"Identify the key criteria for evaluating options related to {topic} based on the following information:\n\n{search_results}"

                elif action["type"] == "EVALUATE_OPTIONS":
                    criteria = self.get_belief(f"criteria_{topic}")
                    prompt = f"Evaluate the different options for {topic} against the following criteria:\n\nCriteria:\n{criteria}\n\nInformation:\n{search_results}"

                elif action["type"] == "DECIDE" or action["type"] == "REPORT":
                    evaluation = self.get_belief(f"evaluation_{topic}")
                    prompt = f"Make a final decision or recommendation about {topic} based on the following evaluation:\n\n{evaluation}"

                # Call AI to process the prompt
                result = await AI_Interaction.generate_text(modelConfig=metadata.defaultTextModel, prompt=prompt)

                # Update beliefs based on action type
                if action["type"] == "ANALYZE":
                    self.update_belief(f"analysis_{topic}", result, "knowledge")

                elif action["type"] == "IDENTIFY_CRITERIA":
                    self.update_belief(f"criteria_{topic}", result, "knowledge")

                elif action["type"] == "EVALUATE_OPTIONS":
                    self.update_belief(f"evaluation_{topic}", result, "knowledge")

                elif action["type"] == "SYNTHESIZE" or action["type"] == "REPORT":
                    self.update_belief(f"synthesis_{topic}", result, "knowledge")

                self.action_completed(True, result)
                return True

            else:
                print(f"[Agent EXECUTE] Unknown action type {action['type']}")
                self.action_completed(False, f"Unknown action type {action['type']}")
                return False

        except Exception as e:
            print(f"[Agent ERROR] Error executing action {e}")
            self.action_completed(False, str(e))
            self.update_belief("failure_reason", str(e), "self_state")
            return False

    async def run(self, max_cycles=10, external_input=None):
        """
        Run the BDI agent perceive-deliberate-plan-execute cycle
        """
        print(f"\n[Agent RUN] Starting BDI agent cycle domain {self.domain}")

        cycle_count = 0
        while cycle_count < max_cycles:
            cycle_count += 1
            print(f"\n--- BDI Cycle {cycle_count} / {max_cycles} ---")

            # Get current status
            status = self.beliefs["self_state"]["status"]
            print(f"[Agent STATUS] Current Status {status}")

            # Check if reached terminal state
            if status in ["COMPLETED", "FAILED"]:
                print(f"[Agent RUN] Terminal state reached {status} Stopping")
                break

            # 1. Perceive
            await self.perceive(external_input)
            external_input = None  # Only use external input first cycle

            # 2. Deliberate
            current_goal = await self.deliberate()

            # 3. Plan
            if current_goal:
                plan_success = await self.plan(current_goal)
                if not plan_success:
                    print("[Agent RUN] Failed to create plan for goal")
                    self.update_belief("status", "FAILED", "self_state")
                    self.update_belief("failure_reason", "Failed to create plan", "self_state")
                    continue

            # 4. Execute
            await self.execute()

            # Update status based on execution
            if self.intentions["plan_status"] == "COMPLETED":
                self.update_belief("status", "COMPLETED", "self_state")
            elif self.intentions["plan_status"] == "FAILED":
                self.update_belief("status", "FAILED", "self_state")

            # Small delay for simulation clarity
            await asyncio.sleep(0.5)

        if cycle_count >= max_cycles:
            print("[Agent WARN] Maximum execution cycles reached Stopping")
            if self.beliefs["self_state"]["status"] not in ["COMPLETED", "FAILED"]:
                self.update_belief("status", "TIMED_OUT", "self_state")

        print(f"[Agent RUN] Execution finished Final Status {self.beliefs['self_state']['status']}")

        # Return final results
        if self.beliefs["self_state"]["status"] == "COMPLETED":
            # Get synthesis results if available
            synthesis = self.get_belief(f"synthesis_{self.domain}")
            if synthesis:
                return synthesis
            return f"Completed goal {self.desires['primary_goal']} but no synthesis available"
        else:
            return f"Agent failed or timed out. Reason: {self.get_belief('failure_reason', 'self_state') or 'Max cycles reached'}"

async def main():
    print("[SCRIPT START] BDI Agent Architecture Demo")

    # Check if API key is configured
    api_key = os.getenv('GOOGLE_AI_STUDIO_API_KEY')
    if not api_key or api_key == 'your_api_key_here':
        print("\n[WARNING] No Google AI Studio API key found in .env file.")
        print("The agent will use fallback text generation instead of the actual API.")
        print("To use the Google AI Studio API, create a .env file with your API key.")
        print("You can copy the .env.template file to .env and add your API key.\n")

    # Define domain and goal
    domain = input("Enter a research domain (default: artificial intelligence ethics): ").strip() or "artificial intelligence ethics"
    goal = input("Enter a research goal (default: Research key principles and provide overview): ").strip() or "Research key principles and provide comprehensive overview"

    print(f"\nInitializing BDI agent with domain: '{domain}' and goal: '{goal}'")

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
    notes_dir = Path("bdi_agent_notes")
    if notes_dir.exists() and any(notes_dir.iterdir()):
        print(f"\nNotes have been saved to the '{notes_dir}' directory.")
        print("Files created:")
        for file in notes_dir.iterdir():
            if file.is_file():
                print(f"  - {file.name}")

    print("[SCRIPT END]")

if __name__ == "__main__":
    asyncio.run(main())
