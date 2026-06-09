from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import jsonOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Tiny/Llama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)


parser = jsonOutputParser()


# template = PromptTemplate(
#     template="Give me the name, age and city of a fictional person \n {format_instructions}",
#     input_variables=[],
#     partial_variables={"format_instructions": parser.get_format_instructions()}
# )


template = PromptTemplate(
    template="Gvie me 5 facts about {topic} \n {format_instructions}",
    input_variables=['topic'],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black holes'})

print(result)
