from langchain_openai import OpenAI
from dotenv import load_dotenv

# import the keys and variable from .evn file.
load_dotenv()

'''
   ****** now we can't use the llm we use the chatboats models ******

# initialize the llm model
llm = OpenAI(
    model='gpt-3.5-turbo-instruct'
)

# it will hit the llm and generate response through the model.
result = llm.invoke("What is the capital of Pakistan")

print(result)
'''

