"""
Test script generator using LLM.
"""
from typing import Dict, Any
import google.generativeai as genai
from src.templates.prompt_templates import get_prompt_template
from src.config.settings import Settings
from loguru import logger

class TestGenerator:
    """Generator for API test scripts."""
    
    def __init__(self, framework: str, model_config: Dict):
        """Initialize test generator."""
        self.framework = framework
        self.settings = Settings()
        self.setup_model(model_config)
        
    def setup_model(self, model_config: Dict):
        """Setup the LLM model."""
        if not self.settings.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        genai.configure(api_key=self.settings.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(model_config["model_name"])
        
    def generate(self, endpoint: str, spec_data: Dict, functionality_description: str) -> str:
        """Generate test script for specified endpoint."""
        try:
            # Parse endpoint
            method, path = endpoint.split(" ", 1)
            endpoint_details = spec_data["paths"][path][method.lower()]
            
            # Get prompt template
            system_prompt, prompt_template = get_prompt_template(self.framework)
            
            # Format prompt
            prompt = prompt_template.format(
                method=method,
                path=path,
                summary=endpoint_details.get('summary', ''),
                parameters=endpoint_details.get('parameters', []),
                request_body=endpoint_details.get('requestBody', {}),
                responses=endpoint_details.get('responses', {}),
                functionality_description=functionality_description
            )

            # Generate test script with system prompt
            response = self.model.generate_content(
                contents=system_prompt + prompt
            )
            return response.text

            
        except Exception as e:
            logger.error(f"Error generating test script: {e}")
            raise