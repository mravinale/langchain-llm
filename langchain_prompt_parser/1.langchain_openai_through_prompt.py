# !pip install python-dotenv
# !pip install openai
# !pip install --upgrade langchain

import os
import openai

from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm_model = "gpt-3.5-turbo"

def init():
    _ = load_dotenv(find_dotenv())  # read local .env file
    openai.api_key = os.environ["OPENAI_API_KEY"]
    print(openai.api_key)


def get_completion(input, style,  prompt):
    # To control the randomness and creativity of the generated
    # text by an LLM, use temperature = 0.0
    chat = ChatOpenAI(
        temperature=0.0,
        model=llm_model)

    prompt_template = ChatPromptTemplate.from_template(prompt)

    customer_messages = prompt_template.format_messages(
        style=style,
        text=input)

    # Call the LLM to translate to the style of the customer message
    customer_response = chat(customer_messages)

    return customer_response.content


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    init()

    input = """
    Arrr, I be fuming that me blender lid 
    flew off and splattered me kitchen walls 
    with smoothie! And to make matters worse, 
    the warranty don't cover the cost of 
    cleaning up me kitchen. I need yer help 
    right now, matey!
    """

    style = """American English in a calm and respectful tone"""

    prompt = f"""
    Translate the text
    that is delimited by triple backticks 
    into a style that is {style}:
    ```{input}```
    """

    print("prompt: ", prompt)

    print("result: ", get_completion(input, style, prompt))
