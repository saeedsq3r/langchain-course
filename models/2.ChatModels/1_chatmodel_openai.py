from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
'''
   *** new way of coding ***
# initialize the chatmodel
model = ChatOpenAI(
    model= 'gpt-4o',
    temperature = 0.9, # it will create more creative answers
    max_completion_tokens = 100, # numbers of tokens you want in the answers
)

# it will hit the chatmodel and return the response.
result = model.invoke("What is the capital of Pakistan?")

# print the answer
print(result.content)
'''

''' 
                 ***** Temperature Values ******

         codes                                        Recomended Ranges
Factual answers (math, code, facts)                     0.0 - 0.3
Balanced response (genral OA, explanations)             0.5 - 0.7
Creative writing storytelling, jokes                    0.9 - 1.2
Maximum Randomness (wild ideas, brainstroming)          1.5+
'''



