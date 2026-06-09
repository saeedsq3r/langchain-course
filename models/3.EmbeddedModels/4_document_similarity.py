from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedings = OpenAIEmbeddings(model = 'text-embeding-3-large', dimensions=300)

document = [
    'first document',
    'second document',
    'third document'
]

query = 'tell me about virat kohli'

doc_embeding = embedings.embed_documents(document)
query_embeding = embedings.embed_query(query)

scores = cosine_similarity([query_embeding],doc_embeding)

index , score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(document[index])
print("similarity score is: ", score)


