from dotenv import load_dotenv
from google import genai
import os

load_dotenv()
gemini_key = os.getenv("GEMINI_TOKEN")

class GeminiManager:
    def __init__(self, api_key=gemini_key):
        self.client = genai.Client(api_key = api_key)

    def prompt(self, input_text):
        response = self.client.models.generate_content(
            model = "gemini-3-pro-preview",
            contents = input_text,
        )
        return response.json()
