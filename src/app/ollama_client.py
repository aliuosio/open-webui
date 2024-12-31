import traceback
import ollama
import time

BASE_URL = "http://ollama:11434/api/generate"


def main():
    time.sleep(5)
    ollama.BASE_URL = BASE_URL
    try:
        print("Sending prompt to Ollama...")
        response = ollama.chat(model='llama3.2:3b', messages=[
            {
                'role': 'user',
                'content': 'Hello! Can you introduce yourself?'
            }
        ])
        if response.status_code == 200:
            message_content = response.get('message', {}).get('content')
            if message_content:
                print("\nOllama's response:")
                print(message_content)
            else:
                print("Unexpected response format.")
        else:
            print(f"Request failed with status code {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()
