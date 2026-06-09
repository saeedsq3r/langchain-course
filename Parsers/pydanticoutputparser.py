from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Tiny/Llama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

class Person(BaseModel):

    name: str = Field(description='Name of the person')
    age: int = Field(gt=18,description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = "Genarate the name, age and city of a ficitional {place} person \n {format_instruction}",
    input_variables =['place'],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
)


chain = template | model | parser

result = chain.invoke({'place':'pakistani'})

print(result)

# prompt = template.invoke({'place': 'pakistani'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)