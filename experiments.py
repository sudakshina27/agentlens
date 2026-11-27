import os
from dotenv import load_dotenv
from openai import OpenAI
import time

load_dotenv()

model = os.getenv("OPENAI_MODEL")

client = OpenAI()

start = time.perf_counter()
response = client.responses.create(
    model=model,
    input=[
        {"role": "user", "content": "My name is Sudakshina."},
        {"role": "assistant", "content": "Nice to meet you, Sudakshina!"},
        {"role": "user", "content": "What's my name?"},
    ],
)
latency = time.perf_counter() - start

print(response.output_text)
print(f"Input tokens: {response.usage.input_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
print(f"Total tokens: {response.usage.total_tokens}")
print(f"Latency: {latency:.2f} seconds")
#print(response)