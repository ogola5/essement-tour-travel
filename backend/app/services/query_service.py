# backend/app/services/query_service.py
from app.llm.gemini import GeminiLLM
from app.llm.prompts import TRAVEL_PROMPT_TEMPLATE

class QueryService:
    """Service for processing user queries with LLM integration."""
    
    @staticmethod
    async def process_query(question: str) -> str:
        """
        Processes a user query using the Gemini LLM.
        
        Args:
            question: The user's question.
        
        Returns:
            The LLM-generated response in markdown.
        
        Raises:
            Exception: If the LLM request fails.
        """
        llm = GeminiLLM()
        prompt = TRAVEL_PROMPT_TEMPLATE.format(question=question)
        return await llm.generate_response(prompt)