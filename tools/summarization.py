from tools.ai_interaction import AI_Interaction

class SummarizationTool:
    """
    Tool for summarizing text using AI models.
    """
    def __init__(self):
        print("[Tool INFO] SummarizationTool initialized")
    
    async def execute(self, text_to_summarize: str, topic_context: str = None, max_length: int = 200) -> str:
        print(f"[Tool ACTION] Summarizing text related to '{topic_context}' (max length: {max_length})")
        
        try:
            # Create a summarization prompt
            prompt = f"Summarize the following text concisely (max {max_length} words), focusing on '{topic_context}':\n\n{text_to_summarize}"
            
            # Use AI_Interaction to generate the summary
            from config.metadata import metadata
            summary = await AI_Interaction.generate_text(modelConfig=metadata.defaultTextModel, prompt=prompt)
            
            print("[Tool SUCCESS] Summarization complete")
            return summary
            
        except Exception as e:
            print(f"[Tool ERROR] Summarization failed: {e}")
            return f"Error during summarization: {e}"
