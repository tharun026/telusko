import os
from dotenv import load_dotenv
import requests

def main():
    load_dotenv()
    print("Hello from demo!")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    uri = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {gemini_api_key}"
    }

    print("headers:", headers)

    payload = {
        "model": "gemini-2.5-flash",
        "messages": [
            {"role": "user", "content": "what is the best movie of the year 2025 across the world"}
        ]
    }

    print("payload:", payload)

    response = requests.post(uri, headers=headers, json=payload)
    print("response:", response.json())

if __name__ == "__main__":
    main()
