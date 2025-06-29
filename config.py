# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Default app configuration

DEFAULT_LANGUAGE = "en"
CHUNK_SIZE = 200
TOP_K = 3