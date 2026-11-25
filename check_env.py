import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

if not key:
    print("OPENAI_API_KEY is missing. Add it to .env")
else:
    print(f"API Key found: {key[:6]}...")