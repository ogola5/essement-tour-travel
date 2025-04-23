# backend/app/llm/base.py
from abc import ABC, abstractmethod

class BaseLLM(ABC):
    """Abstract base class for LLM integrations."""
    
    @abstractmethod
    async def generate_response(self, prompt: str) -> str:
        """Generates a response for the given prompt."""
        pass