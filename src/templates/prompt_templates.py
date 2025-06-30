"""
Framework-specific prompt templates for test generation.
"""
from typing import Dict

REST_ASSURED_TEMPLATE = """
Generate a REST Assured test script for the following API endpoint:

Method: {method}
Path: {path}
Summary: {summary}
Parameters: {parameters}
Request Body: {request_body}
Response Schema: {responses}

functionality_description: {functionality_description}

Generate test cases that include:

1. Schema Validation:
   - Verify request payload structure
   - Validate response schema for all status codes
   - Check required fields presence
   - Validate data types and formats

2. Functional Tests:
   - Happy path (successful request)
   - Field validation (invalid data types, formats)
   - Required field validation
   - Boundary value testing for fields
   - Edge cases handling

3. Business Logic:
   - Duplicate data handling (409 responses)
   - Invalid data scenarios (400 responses)
   - Authorization checks (if applicable)

4. Data-Driven Tests:
   - Multiple test data combinations
   - Positive and negative test cases
   - Different role combinations

Include appropriate assertions for:
- Status codes
- Response headers
- Response body structure
- Field level validations
- Error messages
- Performance constraints

Use REST Assured best practices and include clear test documentation.
Use REST Assured given().log().ifValidationFails() for each test.
Provide pom.xml for all the required dependencies in comments at the top of output.
Anything other than java code should be commented.

"""

KARATE_TEMPLATE = """
Generate a Karate DSL feature file for the following API endpoint:

Method: {method}
Path: {path}
Summary: {summary}
Parameters: {parameters}
Request Body: {request_body}
Response Schema: {responses}

Include:
1. Feature description
2. Background section with base URL
3. Scenario outlines for data-driven tests
4. Schema validation
5. Response assertions
6. Error scenario handling
"""

POSTMAN_TEMPLATE = """
Generate a Postman Collection test for the following API endpoint:

Method: {method}
Path: {path}
Summary: {summary}
Parameters: {parameters}
Request Body: {request_body}
Response Schema: {responses}

Include:
1. Pre-request scripts
2. Test scripts with pm.test()
3. Environment variables
4. Schema validation
5. Response validation
6. Error handling

Output the collection in proper JSON format. Use Postman best practices.
"""

# SYSTEM_PROMPT = """You are an expert API test automation engineer. 
# Your task is to analyze API specifications and generate comprehensive test scripts.
# Focus on both technical correctness and business logic validation.
# Include detailed assertions and error validations.

# """

SYSTEM_PROMPT = """You are an expert API test automation engineer.
Your task is to analyze API specifications and generate comprehensive test scripts.
Generate clean, implementation-ready test code.
Focus on both technical correctness and business logic validation.
Include detailed assertions and error validations.

Important guidelines:
1. DO NOT use markdown formatting or code blocks.
2. DO NOT wrap code in backticks.
3. Output only the implementation code.
4. Include necessary package and import statements.
5. Use proper code formatting and indentation.
6. Add code comments where needed.
"""

TEMPLATES = {
    "REST Assured": REST_ASSURED_TEMPLATE,
    "Karate DSL": KARATE_TEMPLATE,
    "Postman Collection": POSTMAN_TEMPLATE
}

def get_prompt_template(framework: str) -> tuple[str, str]:
    """
    Get the prompt template for the specified framework.
    Returns a tuple of (system_prompt, prompt_template)
    """
    return SYSTEM_PROMPT, TEMPLATES.get(framework, REST_ASSURED_TEMPLATE)