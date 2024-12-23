import requests
import json

url = "http://ollama:11434/api/generate"

headers = {
    "Content-Type": "application/json",
}

payload = {
    "model": "llama3.2:latest",
    "prompt": "What is water made of?"
}

try:
    response = requests.post(url, headers=headers,  data=json.dumps(payload))
    response.raise_for_status()  # Raise an exception for HTTP errors
    
    # Debug raw content
    print("Raw Response Content:", response.json)
    
    # Try parsing JSON
    try:
        data = response.json()
        print("JSON Response:", data)
    except ValueError:
        print("Response is not valid JSON. Raw response:", response.text)
except requests.exceptions.RequestException as e:
    print(f"HTTP Request Error: {e}")
