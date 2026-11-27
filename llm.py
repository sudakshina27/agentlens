import os
import sys
import time

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = os.getenv("OPENAI_MODEL")
if not MODEL:
    sys.exit("Error: OPENAI_MODEL is not set. Add it to your .env file.")

client = OpenAI()


def ask_llm(prompt, instructions=None):
    """Send a prompt to the model, print the answer and stats, and return the response.
    Prompt can be a plain string or a list of {"role": ..., "content": ...} messages."""
    
    start = time.perf_counter()
    response = client.responses.create(
        model=MODEL,
        instructions=instructions,
        input=prompt,
    )
    latency = time.perf_counter() - start

    print(response.output_text)
    print(f"Input tokens:  {response.usage.input_tokens}")
    print(f"Output tokens: {response.usage.output_tokens}")
    print(f"Total tokens:  {response.usage.total_tokens}")
    print(f"Latency:       {latency:.2f} seconds")

    return response
