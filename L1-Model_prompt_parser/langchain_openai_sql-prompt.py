# !pip install python-dotenv
# !pip install openai
# !pip install --upgrade langchain

import os
import openai

from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm_model = "gpt-4"


def init():
    _ = load_dotenv(find_dotenv())  # read local .env file
    openai.api_key = os.environ["OPENAI_API_KEY"]
    print(openai.api_key)


def get_completion(dbscript, query, style, prompt):
    # To control the randomness and creativity of the generated
    # text by an LLM, use temperature = 0.0
    chat = ChatOpenAI(
        temperature=0.0,
        model=llm_model)

    prompt_template = ChatPromptTemplate.from_template(prompt)

    customer_messages = prompt_template.format_messages(
        dbscript=dbscript,
        query = query,
        style = style
    )

    # Call the LLM to translate to the style of the customer message
    customer_response = chat(customer_messages)

    return customer_response.content


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    init()

    dbscript = """
    CREATE DATABASE CompanyEmployeeRelationship;

    USE CompanyEmployeeRelationship;
    
    -- Companies table
    CREATE TABLE companies (
        company_id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        address VARCHAR(255),
        phone VARCHAR(20)
    );
    
    -- Employees table
    CREATE TABLE employees (
        employee_id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        position VARCHAR(255) NOT NULL,
        hiring_date DATE,
        company_id INT,
        FOREIGN KEY (company_id) REFERENCES companies(company_id)
    );
    
    -- Insert example data into companies table
    INSERT INTO companies (name, address, phone) VALUES
    ('Company A', 'Street A, No. 1', '1234567890'),
    ('Company B', 'Street B, No. 2', '0987654321');
    
    -- Insert example data into employees table
    INSERT INTO employees (name, position, hiring_date, company_id) VALUES
    ('John Doe', 'Engineer', '2022-01-15', 1),
    ('Jane Smith', 'Designer', '2021-05-10', 2);
    """

    query = """
    Selecting all the employees from 'Company A'
    """

    style = """
    Best practice, efficient and faster SQL query without any comment or clarification opting joins over sub-queries
    """

    prompt = f"""
    Create an  {style} using the script
    delimited by triple backticks for {query}
    ```{dbscript}```
   
    """

    print("prompt: ", prompt)

    print("result: ", get_completion(dbscript, query, style, prompt))
