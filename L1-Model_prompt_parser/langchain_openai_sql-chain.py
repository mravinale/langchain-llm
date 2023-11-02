# !pip install -r requirements.txt
import os
import openai

from dotenv import load_dotenv, find_dotenv
from langchain.utilities import SQLDatabase
from langchain.chat_models import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain

llm_model = "gpt-4"
pg_uri = f"postgresql+psycopg2://xsfglzen:formrT80AaUkiMVcARze151MlI1V2txB@suleiman.db.elephantsql.com/xsfglzen"



def init():
    _ = load_dotenv(find_dotenv())  # read local .env file
    openai.api_key = os.environ["OPENAI_API_KEY"]
    print(openai.api_key)


def run_query():

    llm = ChatOpenAI(temperature=0, model_name=llm_model)

    db = SQLDatabase.from_uri(pg_uri)
    db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True, top_k=300)

    prompt = """ 
    Given an input question, first create a syntactically correct postgresql query to run,  
    then look at the results of the query and return the answer.  
    The question: {question}
    """

    question = "Provide a query that shows the invoices associated with each sales agent. The resultant table should include the Sales Agent's full name"

    # use db_chain.run(question) instead if you don't have a prompt
    db_chain.run(prompt.format(question=question))

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    init()
    run_query()
