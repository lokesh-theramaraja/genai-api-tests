"""
Tests for the test generator functionality.
"""
import pytest
from src.core.generator import TestGenerator
from src.utils.validators import validate_openapi_spec

@pytest.fixture
def sample_spec_data():
    return {
        "openapi": "3.0.0",
        "info": {
            "title": "Sample API",
            "version": "1.0.0"
        },
        "paths": {
            "/users": {
                "post": {
                    "summary": "Create a user",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "username": {"type": "string"},
                                        "email": {"type": "string"}
                                    }
                                }
                            }
                        }
                    },
                    "responses": {
                        "201": {
                            "description": "User created"
                        }
                    }
                }
            }
        }
    }

def test_validate_openapi_spec(sample_spec_data):
    """Test OpenAPI specification validation."""
    assert validate_openapi_spec(sample_spec_data) is True
    
    # Test invalid spec
    invalid_spec = {"paths": {}}
    assert validate_openapi_spec(invalid_spec) is False

def test_generator_initialization():
    """Test TestGenerator initialization."""
    framework = "REST Assured"
    model_config = {
        "model_name": "gemini-pro",
        "api_key": "test-key"
    }
    
    generator = TestGenerator(framework, model_config)
    assert generator.framework == framework