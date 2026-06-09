from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

embeding = OpenAIEmbeddings(model='text-embeding-3-large', dimensions=32)

result = embeding.embed_query("islamabad is capital of pakistan.")

print(str(result))





