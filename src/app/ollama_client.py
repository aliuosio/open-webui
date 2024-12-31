import traceback
import ollama
import time


def main():
    time.sleep(5)

    ollama.BASE_URL = "http://ollama:11434/api/generate"

    try:
        print("Sending prompt to Ollama...")
        response = ollama.chat(model='llama3.2', messages=[
            {
                'role': 'user',
                'content': 'Hello! Can you introduce yourself?'
            }
        ])

        print("\nOllama's response:")
        print(response['message']['content'])
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()