# cliGPT: A Way to Access OpenAI Models from the CLI
I created cliGPT because I wanted to stop having to launch a browser every time I wanted to send a simple request to ChatGPT.

## How to Install?
You need an [OpenAI API key](https://platform.openai.com/api-keys) for this program to work.

### On Windows:
1. Download the executable from the [release page](https://git.jisoonet.com/publicprojects/cligpt/-/releases).
2. Run `set OPENAI_API_KEY=your_api_key_here` to set up your OpenAI API key as an Environment Variable.
3. Run it from the CLI with `./cligpt`.
4. Optionally add it to PATH for ease of use.

### On Linux:
1. Download the executable from the [release page](https://git.jisoonet.com/publicprojects/cligpt/-/releases).
2. Run `chmod +x cligpt` to make it executable.
3. Run `export OPENAI_API_KEY=your_api_key_here` to set up your OpenAI API key as an Environment Variable.
4. Run it from the CLI with `./cligpt`.
5. Optionally add it to PATH for ease of use with `mv cligpt /usr/local/bin/`.

## Features

### `-help` or `-h`
Displays all of the available commands.

### `-model` or `-m`
Allows you to select a specific [OpenAI model](https://platform.openai.com/docs/models), defaults to `gpt-4`.

### `-exit` or `-e`
Allows you to gracefully exit the program.
