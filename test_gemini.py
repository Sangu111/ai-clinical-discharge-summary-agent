from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("Key found:", bool(api_key))
print("First 10 chars:", api_key[:10] if api_key else "None")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say OK"
)

print(response.text)