import requests
import json

url = "http://ollama:11434/api/generate"

headers = {
    "Content-Type": "application/json",
}

payload = {
    "model": "llama3.2:3b",
    "prompt": "What is water made of?",
    "stream": False,
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Try parsing JSON
    try:
        result = json.loads(response.text)
        print('Model: '+payload['model'])
        print('Prompt: '+payload['prompt'])
        print('Result')
        print(result['response'])
    except ValueError:
        print("Response is not valid JSON. Raw response:", response.text)
except requests.exceptions.RequestException as e:
    print(f"HTTP Request Error: {e}")


# curl http://localhost:11434/api/generate -d '{ "model": "llama3.2:3b", "prompt": "What is water made of?" }'