import requests
import time

start = time.time()

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": "What is Python?",
        "stream": False
    },
    timeout=600
)

print("Time:", time.time() - start)
print(response.json())