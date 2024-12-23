import requests

url = "http://ollama:11434/api/generate"  # Adjust HOST if needed
payload = {
    "model": "jimscard/blackhat-hacker",
    "prompt": "2+2 equals"
}

try:
    response = requests.post(url, json=payload)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
