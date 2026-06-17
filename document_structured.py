from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
text = """ 
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # grade is a float (like 8.5 or 9.2)

    def get_details(self):
    return self.name

    def is_passing(self):
    return self.grade >= 6.0
# Example usage
student1 = Student("saeed", 20, 8.2)
print(student1.get_details())

if student1.is_passing():
    print("The student is passing.")
else:
    print("The student is not passing.")

 """

# Perform the split
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])


'''
            python code splitting
First, try to split along class definitions
"\nclass",
"\ndef",
"\n\tdef",
Now split by the normal type of lines
"\n\n",
"\n",
" ",
"",
'''


'''
            markdown file splittings
First, try to split along Markdown headings (starting with level 2)
"\n#{1,6}",
Note the alternative sysntax for heading (below) is not handled here
Heading level 2
------------------
End of code block
"```\n",
Horizontal lines
"\n\\n*\\*\\*+\n",
"\n---+\n",
"\n___+\n",
Note that this splitter doesn't handle horizontal lines defined
by *three or more* of ***, ---, or ___, but this is not handled
"\n\n",
"\n",
" ",
"",
'''