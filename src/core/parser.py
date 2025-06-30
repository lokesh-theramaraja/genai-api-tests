"""
OpenAPI specification parser.
"""
from typing import Any, Dict
import yaml
import json
from pathlib import Path
from loguru import logger

class OpenAPIParser:
    """Parser for OpenAPI/Swagger specifications."""
    
    def parse(self, file_obj: Any) -> Dict:
        """Parse OpenAPI specification file."""
        try:
            filename = Path(file_obj.name)
            if filename.suffix in ['.yaml', '.yml']:
                return yaml.safe_load(file_obj)
            elif filename.suffix == '.json':
                return json.load(file_obj)
            else:
                raise ValueError(f"Unsupported file type: {filename.suffix}")
        except Exception as e:
            logger.error(f"Error parsing OpenAPI spec: {e}")
            raise