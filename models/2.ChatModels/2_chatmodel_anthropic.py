from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

# load the keys from .env file
load_dotenv()

# load the model selected
model = ChatAnthropic(
    model = 'claude-3-5-sonnet-20241022'
)

# hit the model and make the response.
result = model.invoke("What is the capital of Pakistan?")

# print the response from model
print(result.content)
