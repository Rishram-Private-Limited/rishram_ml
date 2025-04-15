import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API key from .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check if API key is loaded
if GEMINI_API_KEY:
    print("API key loaded successfully.")
    # Configure Google Generative AI with API key
    genai.configure(api_key=GEMINI_API_KEY)

    # List available models
    try:
        models = genai.list_models()
        print("Available models:")
        for model in models:
            print(model.name)
    except Exception as e:
        print(f"Error fetching models: {e}")

else:
    print("Error: API key not found. Check your .env file.")
