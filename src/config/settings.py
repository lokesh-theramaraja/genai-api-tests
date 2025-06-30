"""
Application settings and configuration.
"""
from typing import Dict, Any
from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    """Application settings and configuration."""
    
    # API Keys
    OPENAI_API_KEY: str
    GOOGLE_API_KEY: str
    
    # Model Configuration
    MODEL_CONFIG: Dict[str, Any] = {
        "model_name": "gemini-2.0-flash",
        "model_provider": "google_genai",
        "max_input_tokens": 4096,
        "max_output_tokens": 1024,
        "temperature": 0.2
    }
    
    # Framework Configurations
    SUPPORTED_FRAMEWORKS: Dict[str, Dict[str, str]] = {
        "REST Assured": {
            "language": "java",
            "description": "Java-based REST API testing framework",
            "file_extension": ".java"
        },
        "Karate DSL": {
            "language": "feature",
            "description": "BDD-style API testing framework",
            "file_extension": ".feature"
        },
        "Postman Collection": {
            "language": "json",
            "description": "Postman collection format for API testing",
            "file_extension": ".json"
        }
    }
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        case_sensitive = True