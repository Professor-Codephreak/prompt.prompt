import asyncio

# Mock AI_Interaction class for simulation
class AI_Interaction:
    @staticmethod
    async def generate_text(modelConfig, prompt):
        print(f"[AI_Interaction] Generating text with model {modelConfig.get('model_id', 'unknown')}")
        print(f"[AI_Interaction] Prompt: {prompt[:100]}...")  # Show first 100 chars
        await asyncio.sleep(1)  # Simulate API call
        
        # For BDI agent architecture topic
        if "BDI agent architecture" in prompt:
            return """
The Belief-Desire-Intention (BDI) agent architecture is a framework for building intelligent agents based on the philosophical theory of practical reasoning. Key findings include:

1. Core Components: BDI agents maintain three key mental attitudes - Beliefs (knowledge about the world), Desires (goals/objectives), and Intentions (committed plans of action).

2. Practical Reasoning: BDI implements two-step reasoning: deliberation (deciding what goals to achieve) and means-ends reasoning (determining how to achieve them).

3. Implementation: Popular BDI platforms include JACK, Jason, and Jadex, which provide programming languages and runtime environments for BDI agents.

4. Applications: BDI architecture has been successfully applied in autonomous systems, robotics, simulation, and decision support systems.

5. Advantages: BDI offers intuitive modeling of human-like reasoning, separation of concerns, and reactive/deliberative balance.

Current research focuses on extending BDI with learning capabilities, emotional models, and formal verification methods.
"""
        return "Generated summary about the requested topic."

# Mock metadata for simulation
class Metadata:
    def __init__(self):
        self.defaultTextModel = {"model_id": "gemini-2.5-pro-exp-03-25", "temperature": 0.5}
        self.defaultPlannerModel = {"model_id": "gemini-1.5-flash", "temperature": 0.7}

metadata = Metadata()

# WebSearchTool implementation
class WebSearchTool:
    def __init__(self, api_key=None):
        print("[Tool INFO] WebSearchTool initialized")
        pass

    async def execute(self, query: str, max_results=3) -> str:
        print(f"[Tool ACTION] Executing web search for '{query}' max_results {max_results}")
        await asyncio.sleep(1)  # Simulate network delay
        
        # Simulate finding results for BDI
        if "BDI" in query:
            results = [
                "Result one about BDI: The Belief-Desire-Intention (BDI) model is a framework for designing intelligent agents. It was developed by Michael Bratman as a way of explaining future-directed intention.",
                "Result two related BDI: BDI architectures have been implemented in various agent platforms such as JACK, Jason, and Jadex. These platforms provide programming languages and runtime environments for BDI agents.",
                "Result three mentioning BDI: In the BDI model, beliefs represent the informational state of the agent, desires represent the motivational state, and intentions represent the deliberative state of the agent."
            ]
        else:
            results = [
                f"Result one about {query} Details",
                f"Result two related {query} More info",
                f"Result three mentioning {query} Snippet"
            ]
        
        print(f"[Tool SUCCESS] Found {len(results)} results")
        return "\n---\n".join(results[:max_results])

# ResearchAssistantAgent implementation
class ResearchAssistantAgent:
    def __init__(self, topic: str):
        print(f"[Agent INFO] Initializing ResearchAssistantAgent topic '{topic}'")
        self.topic = topic
        self.goal = f"Provide concise summary key findings about '{topic}'"
        self.state = {
            "status": "INITIALIZED",
            "search_query": self.topic,
            "raw_findings": None,
            "summary": None,
            "last_action": None,
            "failure_reason": None,
            "clarification_needed": None
        }
        self.available_tools = {
            "web_search": WebSearchTool(),
            "summarizer": self._create_summarizer_tool()
        }
        print(f"[Agent INFO] Goal set {self.goal}")
        print(f"[Agent INFO] Available tools {list(self.available_tools.keys())}")

    def _create_summarizer_tool(self):
        print("[Tool INFO] SummarizationTool conceptual initialized")
        class SummarizerTool:
            async def execute(self, text_to_summarize, topic_context):
                print(f"[Tool ACTION] Summarizing text related '{topic_context}'")
                summary_prompt = f"Summarize the following text concisely (approx 150 words), focusing on '{topic_context}':\n\n{text_to_summarize}"
                try:
                    summary = await AI_Interaction.generate_text(modelConfig=metadata.defaultTextModel, prompt=summary_prompt)
                    print("[Tool SUCCESS] Summarization complete")
                    return summary
                except Exception as e:
                    print(f"[Tool ERROR] Summarization failed {e}")
                    return "Error during summarization"
        return SummarizerTool()

    def perceive(self, feedback=None):
        print("[Agent PERCEIVE] Perceiving environment")
        if feedback:
            print(f"[Agent PERCEIVE] Received feedback {feedback}")
            if "clarification required" in feedback.lower():
                self.state['status'] = "ASKING_CLARIFICATION"
                self.state['clarification_needed'] = feedback

    async def plan(self) -> str:
        print("[Agent PLAN] Planning next action")
        status = self.state['status']
        action = "COMPLETE"  # Default action

        # Simple state machine logic
        if status == "INITIALIZED": action = "SEARCH"
        elif status == "SEARCHING" and self.state['raw_findings'] is None:
            print("[Agent PLAN] Search failed previously or yielded no results Failing")
            action = "FAIL"; self.state['failure_reason'] = "Search yielded no results or failed"
        elif status == "SEARCHING" and self.state['raw_findings']: action = "SUMMARIZE"
        elif status == "SUMMARIZING" and self.state['summary'] is None:
            print("[Agent PLAN] Summarization failed previously Failing")
            action = "FAIL"; self.state['failure_reason'] = "Summarization failed"
        elif status == "SUMMARIZING" and self.state['summary']:
            if "needs clarification" in self.state['summary'].lower() or "ambiguous" in self.state['summary'].lower():
                action = "ASK_CLARIFICATION"; self.state['clarification_needed'] = "Summary generated but indicates ambiguity or requires clarification"
            else: action = "COMPLETE"
        elif status == "ASKING_CLARIFICATION":
            print("[Agent PLAN] Waiting clarification no input mechanism shown Failing")
            action = "FAIL"; self.state['failure_reason'] = "Requires clarification cannot receive interactive input this example"

        print(f"[Agent PLAN] Decided Action {action}")
        return action

    async def act(self, action: str):
        print(f"[Agent ACT] Executing Action {action}")
        self.state['last_action'] = action
        original_status = self.state['status']  # Store status before action

        try:
            if action == "SEARCH":
                self.state['status'] = "SEARCHING"  # Update status before async call
                query = self.state['search_query']
                search_tool = self.available_tools['web_search']
                findings = await search_tool.execute(query=query)
                self.state['raw_findings'] = findings

            elif action == "SUMMARIZE":
                self.state['status'] = "SUMMARIZING"
                if not self.state['raw_findings']: raise ValueError("Cannot summarize without findings")
                summarizer_tool = self.available_tools['summarizer']
                summary = await summarizer_tool.execute(text_to_summarize=self.state['raw_findings'], topic_context=self.topic)
                self.state['summary'] = summary

            elif action == "ASK_CLARIFICATION":
                self.state['status'] = "WAITING_FOR_CLARIFICATION"
                print(f"[Agent ACT] Clarification required {self.state.get('clarification_needed', 'Please provide more details')}")

            elif action == "COMPLETE":
                self.state['status'] = "COMPLETE"
                print(f"[Agent ACT] Goal achieved Final Summary\n{self.state['summary']}")

            elif action == "FAIL":
                self.state['status'] = "FAILED"
                print(f"[Agent ACT] Action resulted failure state Reason {self.state.get('failure_reason', 'Unknown')}")

            else:
                print(f"[Agent WARN] Unknown action {action} requested")
                self.state['status'] = original_status  # Revert status if action unknown

        except Exception as e:
            print(f"[Agent ERROR] Error during action {action} {e}")
            self.state['status'] = "FAILED"; self.state['failure_reason'] = str(e)

    async def run(self, max_cycles=10):
        print(f"\n[Agent RUN] Starting execution cycle goal {self.goal}")
        cycle_count = 0
        while cycle_count < max_cycles:
            cycle_count += 1
            print(f"\n--- Cycle {cycle_count} / {max_cycles} ---")
            current_status = self.state['status']
            print(f"[Agent STATUS] Current Status {current_status}")

            if current_status in ["COMPLETE", "FAILED"]:
                print(f"[Agent RUN] Terminal state reached {current_status} Stopping")
                break

            # One Perceive simple version here
            self.perceive()  # In more complex agent might take external input

            # Two Plan
            next_action = await self.plan()

            # Three Act
            await self.act(next_action)

            # Small delay simulation clarity
            await asyncio.sleep(0.5)

        if cycle_count >= max_cycles:
            print("[Agent WARN] Maximum execution cycles reached Stopping")
            if self.state['status'] not in ["COMPLETE", "FAILED"]: self.state['status'] = "TIMED_OUT"

        print(f"[Agent RUN] Execution finished Final Status {self.state['status']}")
        if self.state['status'] == 'COMPLETE': return self.state['summary']
        else: return f"Agent failed timed out Reason {self.state.get('failure_reason', 'Max cycles reached')}"

async def main():
    print("[SCRIPT START] Research Assistant Agent Demo")

    # Define research topic
    topic_to_research = "BDI agent architecture"

    # Instantiate agent
    research_agent = ResearchAssistantAgent(topic=topic_to_research)

    # Run agent main loop
    final_result = await research_agent.run(max_cycles=5)

    print("\n--- Agent Final Output ---")
    print(final_result)
    print("--------------------------")
    print("[SCRIPT END]")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
