import requests
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
openai_key = os.getenv("OPENAI_TOKEN")

class GPTManager:
    def __init__(self, api_key=openai_key):
        self.client = OpenAI(api_key = api_key)

    def prompt(self, input_text):
        response = self.client.responses.create(
            model = "gpt-5-nano",
            input = input_text,
        )
        return response.json()
