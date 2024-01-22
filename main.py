from openai import OpenAI
from config import *

# api key setup
client = OpenAI(api_key=API_KEY_OPENAI)

# request to openai
stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": ""}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
