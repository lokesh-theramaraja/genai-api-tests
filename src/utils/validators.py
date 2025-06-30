"""
Validation utilities for API test generation.
"""
from typing import Any
from pathlib import Path

def validate_file_type(file_obj: Any) -> bool:
    """
    Validate if the uploaded file is of supported type.
    
    Args:
        file_obj: The uploaded file object
        
    Returns:
        bool: True if file type is supported, False otherwise
    """
    allowed_extensions = {'.yaml', '.yml', '.json'}
    return Path(file_obj.name).suffix.lower() in allowed_extensions

def validate_openapi_spec(spec_data: dict) -> bool:
    """
    Validate if the parsed data is a valid OpenAPI specification.
    
    Args:
        spec_data: Parsed OpenAPI specification data
        
    Returns:
        bool: True if valid OpenAPI spec, False otherwise
    """
    required_fields = {'openapi', 'info', 'paths'}
    return all(field in spec_data for field in required_fields)