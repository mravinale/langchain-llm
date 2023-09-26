# !pip install python-dotenv
# !pip install openai

import os
import openai

from dotenv import load_dotenv, find_dotenv

llm_model = "gpt-3.5-turbo"


def init():
    _ = load_dotenv(find_dotenv())  # read local .env file
    openai.api_key = os.environ["OPENAI_API_KEY"]
    print(openai.api_key)


def get_completion(prompt, model=llm_model):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    init()
    get_completion("What is 1+1?")
