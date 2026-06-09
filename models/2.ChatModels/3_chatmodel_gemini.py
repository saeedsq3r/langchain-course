from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# load .env file keys
load_dotenv()

# loading model
model = ChatGoogleGenerativeAI(
    model = 'gemini-1.5-pro'
)

# hit the model and take response.
result = model.invoke("What is the capital of Pakistan?")

# print the model response.
print(result.content)