# cliGPT: A Way to Access OpenAI Models from the CLI
I created cliGPT because I wanted to stop having to launch a browser every time I wanted to send a simple request to ChatGPT.
The program utilizes the [Streaming](https://platform.openai.com/docs/api-reference/streaming) function of the OpenAI API to automatically send answers in chunks, ensuring that you don't have to wait for long responses to generate all at once.

## How to Install?
You need an [OpenAI API key](https://platform.openai.com/api-keys) for this program to work.

### On Windows:
1. Download the executable from the [release page](https://git.jisoonet.com/publicprojects/cligpt/-/releases).
2. Run `set OPENAI_API_KEY=your_api_key_here` to set up your OpenAI API key as an Environment Variable.
3. Run `./cligpt` to execute the program.
4. Optionally add it to PATH for ease of use.

### On Linux:
1. Download the executable from the [release page](https://git.jisoonet.com/publicprojects/cligpt/-/releases).
2. Run `chmod +x cligpt` to make it executable.
3. Run `export OPENAI_API_KEY=your_api_key_here` to set up your OpenAI API key as an Environment Variable.
4. Run `./cligpt` to execute the program.
5. Optionally add it to PATH for ease of use with `mv cligpt /usr/local/bin/`.

### Build from source:
1. Run `git clone https://git.jisoonet.com/publicprojects/cligpt.git`.
2. Run `cd cligpt` to change into the cloned directory.
3. Run `./main.py` to verify that you have all the dependencies installed.
4. Run `pyinstaller --onefile main.py` to compile the program.
5. Follow step **2.** for your respective OS.

## Features

### `-help` or `-h`
Displays all of the available commands.

### `-model` or `-m`
Allows you to select a specific [OpenAI model](https://platform.openai.com/docs/models), defaults to `gpt-4`.

### `-exit` or `-e`
Allows you to gracefully exit the program.
