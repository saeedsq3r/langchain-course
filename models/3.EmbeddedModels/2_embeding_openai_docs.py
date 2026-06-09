from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()


document = [
    'first document'
    'Second document',
    'Third document',
]

embeding = OpenAIEmbeddings(model='text-embeding-3-large', dimensions=32)
result = embeding.embed_documents(document)



print(str(result))
