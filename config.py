import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

import google.generativeai as genai

# API Configuration
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

if not GOOGLE_API_KEY:
    raise EnvironmentError("ERROR: GOOGLE_API_KEY not found in .env file or environment variables. This key is required for the application to run.")
genai.configure(api_key=GOOGLE_API_KEY)
