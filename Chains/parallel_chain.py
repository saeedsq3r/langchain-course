from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatOpenAI()

model2 = ChatAnthropic(model_name='claude-3-7-sonnet-20250219')

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)
prompt2 = PromptTemplate(
    template='Generate 5 short question from the follwing text \n {text}',
    input_variables=['text']
)
prompt3 = PromptTemplate(
    template='Merge th provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz} ',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
Linear Regression

Linear regression is one of the most fundamental and widely used algorithms in the field of machine learning and statistics. It is a supervised learning technique that is used to predict a continuous numerical value by finding the relationship between one or more independent variables (features) and a dependent variable (target). The main goal of linear regression is to fit a straight line through the data points in such a way that the difference between the predicted values and the actual values is as small as possible. This line is often represented by the mathematical equation **y = mx + b**, where **y** is the predicted output, **x** is the input feature, **m** is the slope of the line, and **b** is the intercept. In the case of multiple input variables, the equation expands to include additional coefficients for each feature. Linear regression works by calculating the optimal values of these coefficients using methods such as the Least Squares Method, which minimizes the sum of the squared differences between actual and predicted values. Because of its simplicity and interpretability, linear regression is commonly used as a starting point for many data science projects and serves as the foundation for understanding more advanced machine learning algorithms.

Linear regression has numerous real-world applications across various industries. In the real estate sector, it can be used to estimate house prices based on factors such as size, location, number of bedrooms, and age of the property. In finance, it helps predict stock prices, sales trends, or future revenues based on historical data. Businesses often use linear regression for demand forecasting, customer spending prediction, and marketing analysis. In healthcare, researchers use it to study relationships between variables, such as the impact of age, weight, or lifestyle factors on blood pressure or disease risk. The algorithm assumes that there is a linear relationship between the independent and dependent variables, that the errors are normally distributed, and that the variance of the errors remains constant across observations. Although these assumptions may not always hold in practical situations, linear regression often provides a good approximation and valuable insights into the data.

There are two main types of linear regression: **Simple Linear Regression** and **Multiple Linear Regression**. Simple linear regression uses only one independent variable to predict the target variable, while multiple linear regression uses two or more independent variables. The performance of a linear regression model is commonly evaluated using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and the Coefficient of Determination (**R² Score**), which measures how well the model explains the variability of the data. One of the greatest advantages of linear regression is that it is easy to implement, computationally efficient, and highly interpretable, making it an excellent choice for beginners learning machine learning. However, it also has limitations, such as sensitivity to outliers and the inability to capture complex nonlinear relationships. Despite these limitations, linear regression remains one of the most important and widely applied algorithms in data analysis, predictive modeling, and artificial intelligence, forming the basis for many advanced statistical and machine learning techniques.


"""
result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()