# backend/app/llm/deepseek.py
import requests
from app.core.config import settings

class DeepSeekLLM:
    """Interface for interacting with the DeepSeek LLM API."""
    
    def __init__(self):
        self.api_key = settings.deepseek_api_key
        self.base_url = "https://api.deepseek.com/v1/completions"
    
    async def generate_response(self, prompt: str) -> str:
        """
        Generates a response using the DeepSeek LLM.
        
        Args:
            prompt: The prompt to send to the LLM.
        
        Returns:
            The generated response text.
        
        Raises:
            Exception: If the API request fails or the API key is missing.
        """
        if not self.api_key:
            return "Mock response: Please configure DEEPSEEK_API_KEY"
        
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            data = {
                "prompt": prompt,
                "model": "deepseek-free",
                "max_tokens": 500,
                "temperature": 0.7
            }
            response = requests.post(self.base_url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()["choices"][0]["text"]
        except Exception as e:
            raise Exception(f"DeepSeek API error: {str(e)}")