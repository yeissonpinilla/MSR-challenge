import requests
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
openai_key = os.getenv("OPENAI_TOKEN")

class GPTManager:
    def __init__(self, api_key=openai_key):
        self.client = OpenAI(api_key = api_key)

    def prompt(self, input_text, params=None):
        response = self.client.responses.create(
            model = "gpt-5-nano",
            input = "this is a test, am I using my credits?",
        )
        return response.json()

    def post(self, endpoint, data=None):
        url = f"{self.client}/{endpoint.lstrip('/')}"
        headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
