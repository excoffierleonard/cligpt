from openai import OpenAI
import os

# Configuration
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
OPENAI_MODEL = "gpt-4-1106-preview"

if not OPENAI_API_KEY:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

def main():
    # API key setup
    client = OpenAI(api_key=OPENAI_API_KEY)

    while True:
        try:
            # User input
            user_input = input("Enter your message (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break

            # Request to OpenAI
            stream = client.chat.completions.create(
                model=OPENAI_MODEL,
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
