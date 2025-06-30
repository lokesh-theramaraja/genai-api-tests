# API Test Generator 🧪

A Streamlit web application that automatically generates API test scripts from OpenAPI/Swagger specifications using Google's Gemini LLM.

## Features

- Upload OpenAPI/Swagger files (YAML/JSON)
- Support for multiple test frameworks:
  - REST Assured (Java)
  - Karate DSL
  - Postman Collections
- Interactive web interface
- Automatic schema validation
- Data-driven test generation
- Error scenario handling

## Prerequisites

- Python 3.8+
- Google Gemini API key
- OpenAI API key (optional)

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and add your API keys:
```bash
cp .env.example .env
```

## Usage

1. Start the application:
```bash
streamlit run main.py
```

2. Open your browser to the displayed URL (typically http://localhost:8501)

3. Upload your OpenAPI/Swagger specification

4. Select your preferred test framework

5. Choose the API endpoint to test

6. Generate and download your test scripts

## Project Structure

```
demo-project/
├── src/
│   ├── config/         # Configuration settings
│   ├── core/           # Core business logic
│   ├── templates/      # Prompt templates
│   └── utils/          # Utility functions
├── tests/              # Test files
├── main.py            # Main application
└── requirements.txt   # Project dependencies
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.