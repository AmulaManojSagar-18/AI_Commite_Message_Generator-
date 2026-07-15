# llm.py
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

# We load the API key from the .env file.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_commit_message(diff, prompt_template):
    prompt = prompt_template.format(diff=diff)

    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=prompt
    )

    return response.text.strip()