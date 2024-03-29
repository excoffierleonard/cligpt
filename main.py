import json
import os
from pathlib import Path
from openai import OpenAI

home_dir = Path.home()
config_dir = home_dir / '.cligpt'
config_dir.mkdir(exist_ok=True)
config_file = config_dir / 'settings.json'

def load_config():
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        config = {}
        save_config(config)
    return config

def save_config(config):
    with open(config_file, 'w') as file:
        json.dump(config, file, indent=4)

def update_model(config):
    user_model = input("Enter a new OpenAI model (press Enter for default 'gpt-4'): ")
    config['model'] = user_model.strip() or 'gpt-4'
    save_config(config)
    print(f"Model updated to {config['model']}")

def print_help():
    help_text = """
    Available commands:
    -help or -h: Display this help message.
    -model or -m: Change the OpenAI model. List of available models: https://platform.openai.com/docs/models
    -exit or -e: Exit the program.

    Setting API Key:
    Linux: export OPENAI_API_KEY='your-api-key'
    Windows: set OPENAI_API_KEY=your-api-key

    Note: Replace 'your-api-key' with your actual OpenAI API key.
    """
    print(help_text)

def main():
    config = load_config()
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

    if not OPENAI_API_KEY:
        raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

    if 'model' not in config or not config['model']:
        config['model'] = 'gpt-4'
        save_config(config)

    client = OpenAI(api_key=OPENAI_API_KEY)

    try:
        while True:
            print("\nEnter your message (type '-h' or '-help' for help): ")
            user_input = input()

            if user_input.lower() in ['-help', '-h']:
                print_help()
                continue
            if user_input.lower() in ['-model', '-m']:
                update_model(config)
                continue
            if user_input.lower() in ['-exit', '-e']:
                break

            stream = client.chat.completions.create(
                model=config['model'],
                messages=[{"role": "user", "content": user_input}],
                stream=True,
            )

            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    print(chunk.choices[0].delta.content, end="")
            print()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
