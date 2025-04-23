# backend/app/llm/gemini.py
import requests
from app.core.config import settings
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GeminiLLM:
    """Interface for interacting with the Google Gemini API."""
    
    def __init__(self):
        self.api_key = settings.gemini_api_key
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    
    async def generate_response(self, prompt: str) -> str:
        """
        Generates a response using the Google Gemini API.
        
        Args:
            prompt: The prompt to send to the LLM.
        
        Returns:
            The generated response text.
        
        Raises:
            Exception: If the API request fails or the API key is missing.
        """
        if not self.api_key:
            logger.warning("Gemini API key is missing")
            return "Mock response: Please configure GEMINI_API_KEY"
        
        try:
            headers = {
                "Content-Type": "application/json"
            }
            params = {"key": self.api_key}
            data = {
                "contents": [
                    {
                        "parts": [
                            {"text": prompt}
                        ]
                    }
                ],
                "generationConfig": {
                    "temperature": 0.7,
                    "maxOutputTokens": 500
                }
            }
            logger.info(f"Sending request to Gemini API: {data}")
            response = requests.post(self.base_url, json=data, headers=headers, params=params)
            response.raise_for_status()
            result = response.json()
            logger.info(f"Gemini API response: {result}")
            return result["candidates"][0]["content"]["parts"][0]["text"]
        except requests.exceptions.HTTPError as e:
            logger.error(f"Gemini API HTTP error: {str(e)}")
            raise Exception(f"Gemini API error: {str(e)}")
        except Exception as e:
            logger.error(f"Gemini API general error: {str(e)}")
            raise Exception(f"Gemini API error: {str(e)}")