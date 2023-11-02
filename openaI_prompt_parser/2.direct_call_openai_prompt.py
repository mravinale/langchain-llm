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

    customer_email = """
    Arrr, I be fuming that me blender lid \
    flew off and splattered me kitchen walls \
    with smoothie! And to make matters worse,\
    the warranty don't cover the cost of \
    cleaning up me kitchen. I need yer help \
    right now, matey!
    """

    style = """American English \
    in a calm and respectful tone
    """

    prompt = f"""Translate the text \
    that is delimited by triple backticks 
    into a style that is {style}.
    text: ```{customer_email}```
    """

    print("prompt: ", prompt)

    print("result", get_completion(prompt))
