# backend/app/core/config.py
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    """Application configuration settings."""
    app_name: str = "TravelBuddy Q&A"
    frontend_url: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    api_v1_prefix: str = "/api/v1"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()