"""
Main Streamlit application for API test generation.
"""
from typing import Optional, Dict, Any
import streamlit as st
from pathlib import Path
from src.core.parser import OpenAPIParser
from src.core.generator import TestGenerator
from src.config.settings import Settings
from src.utils.validators import validate_file_type, validate_openapi_spec
from loguru import logger

class APITestApp:
    """Main application class for API test generation."""
    
    def __init__(self):
        """Initialize application settings and configurations."""
        self.settings = Settings()
        self.setup_logging()
        self.init_streamlit()
        
    def setup_logging(self):
        """Configure application logging."""
        logger.add(
            "logs/app.log",
            rotation="500 MB",
            level="INFO",
            format="{time} {level} {message}"
        )

    def init_streamlit(self):
        """Initialize Streamlit page configuration."""
        st.set_page_config(
            page_title="API Tests Generator",
            layout="centered",
            initial_sidebar_state="expanded"
        )
        st.title("🚀✨ API Tests Generator")
        st.markdown("""
        This application generates API test scripts from OpenAPI/Swagger specifications.
        It supports multiple test frameworks and provides a user-friendly interface for selecting endpoints and generating tests.
        """)

    def run(self):
        """Run the main application loop."""
        try:
            uploaded_file = self.file_upload_section()
            if uploaded_file:
                self.process_file(uploaded_file)
        except Exception as e:
            logger.error(f"Application error: {e}")
            st.error(f"An error occurred: {str(e)}")

    def file_upload_section(self) -> Optional[Any]:
        """Handle file upload section."""
        return st.file_uploader(
            "Upload OpenAPI/Swagger file",
            type=["yaml", "yml", "json"],
            help="Select a valid OpenAPI/Swagger specification file"
        )
    
    def functionality_input_section(self) -> str:
        """Handle functionality description input."""
        st.subheader("Describe API Functionality")
        return st.text_area(
            "Provide a brief description of the API functionality",
            placeholder="E.g., This API endpoint retrieves user details based on user ID",
            help="This description will be used to enhance the test generation process"
        )

    def process_file(self, uploaded_file: Any):
        """Process the uploaded OpenAPI file."""
        try:
            if not validate_file_type(uploaded_file):
                st.error("Unsupported file type. Please upload a YAML or JSON file.")
                return

            # Parse OpenAPI spec
            parser = OpenAPIParser()
            spec_data = parser.parse(uploaded_file)

            if not validate_openapi_spec(spec_data):
                st.error("The uploaded file is not a valid OpenAPI specification.")
                return

            # user functionality input
            functionality_description = self.functionality_input_section()

            # Framework selection
            framework = self.framework_selection()
            
            # Endpoint selection
            endpoint = self.endpoint_selection(spec_data)
            
            if st.button("Generate Test Script"):
                self.generate_test_script(framework, endpoint, spec_data, functionality_description)
                
        except Exception as e:
            logger.error(f"File processing error: {e}")
            st.error(f"Error processing file: {str(e)}")

    def framework_selection(self) -> str:
        """Handle test framework selection."""
        st.subheader("Select Test Framework")
        return st.selectbox(
            "Choose Framework",
            options=self.settings.SUPPORTED_FRAMEWORKS.keys(),
            help="Select your preferred test framework"
        )

    def endpoint_selection(self, spec_data: Dict) -> str:
        """Handle API endpoint selection."""
        endpoints = [
            f"{method.upper()} {path}"
            for path, methods in spec_data.get("paths", {}).items()
            for method in methods
        ]
        return st.selectbox("Select Endpoint", endpoints)

    def generate_test_script(
        self, 
        framework: str, 
        endpoint: str, 
        spec_data: Dict,
        functionality_description: str
    ):
        """Generate test script based on selected options."""
        with st.spinner("Generating test script..."):
            try:
                generator = TestGenerator(
                    framework=framework,
                    model_config=self.settings.MODEL_CONFIG
                )
                test_script = generator.generate(endpoint, spec_data, functionality_description)
                self.display_results(test_script, framework)
            except Exception as e:
                logger.error(f"Generation error: {e}")
                st.error("Failed to generate test script")

    def display_results(self, test_script: str, framework: str):
        """Display and handle download of generated test script."""
        st.success("✅ Test script generated!")
        
        framework_config = self.settings.SUPPORTED_FRAMEWORKS[framework]
        file_ext = framework_config["file_extension"]
        
        st.code(test_script, language=framework_config["language"])
        
        st.download_button(
            label=f"⬇️ Download {file_ext} File",
            data=test_script,
            file_name=f"test_script{file_ext}",
            mime="text/plain"
        )

if __name__ == "__main__":
    app = APITestApp()
    app.run()