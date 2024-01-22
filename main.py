import json
import os
from openai import OpenAI

# Configuration File Path
CONFIG_FILE = 'settings.json'

# Load or Initialize Configuration
def load_config():
    try:
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
            # Set default model if not present
            config.setdefault('model', 'gpt-4')
            return config
    except FileNotFoundError:
        # Default configuration
        return {'model': 'gpt-4'}

# Save Configuration
def save_config(config):
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file, indent=4)

def main():
    config = load_config()
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

    if not OPENAI_API_KEY:
        raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

    # Prompt for model change if needed
    change_model = input(f"Current model is '{config['model']}'. Do you want to change it? (yes/no): ").lower()
    if change_model == 'yes':
        config['model'] = input("Enter the OpenAI model you want to use: ")
        save_config(config)

    client = OpenAI(api_key=OPENAI_API_KEY)

    while True:
        try:
            user_input = input("Enter your message (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break

            stream = client.chat.completions.create(
                model=config['model'],
                messages=[{"role": "user", "content": user_input}],
                stream=True,
            )

            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    print(chunk.choices[0].delta.content, end="")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
