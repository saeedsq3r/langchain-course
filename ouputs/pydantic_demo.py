# Pydantic is a data validation and data parsing library for Python. It ensures that the data you work with is correct, structured, and type-safe.

# used for data validation in projects

from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
     
     name: str = 'saeed'
     age: Optional[int] = None
     email: EmailStr
     cgpa: float = Field(gt=0,lt=10, default=2.3, description='A decimal value representing the cpga of the student')



new_student = {'age':20, 'email':'abc@gmail.com', 'cgpa':5}

student = Student(**new_student)

# print(student.name)
# print(type(student))
student_dict = dict(student)
student_json = student.model_dump_json()

print(student_dict['age'])