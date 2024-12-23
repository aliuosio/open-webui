import requests

url = "http://ollama:11434/api/generate"  # Adjust HOST if needed
payload = {
    "model": "llama3.2:latest",
    "prompt": "2+2 equals"
}

try:
    response = requests.post(url, json=payload)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
