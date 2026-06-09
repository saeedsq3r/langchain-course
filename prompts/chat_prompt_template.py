from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

# recomended
chat_template = ChatPromptTemplate([
    ('system','Your are a helpfull {domain} expert'),
    ('human','Explain in simple terms, what is {topic}')
])

# not use now
# chat_template = ChatPromptTemplate.from_messages([
#     ('system','Your are a helpfull {domain} expert'),
#     ('human','Explain in simple terms, what is {topic}')
# ])

prompt = chat_template.invoke({'domain':'cricket', 'topic':'dusra'})

print(prompt)