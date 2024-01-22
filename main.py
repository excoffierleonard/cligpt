from openai import OpenAI
from config import API_KEY_OPENAI

def main():
    # API key setup
    client = OpenAI(api_key=API_KEY_OPENAI)

    try:
        # User input
        user_input = input("Enter your message: ")

        # Request to OpenAI
        stream = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[{"role": "user", "content": user_input}],
            stream=True,
        )

        # Process stream
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()