from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('testing_lang.pdf')

docs = loader.load()

splitter1 = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
)

result1 = splitter1.split_documents(docs)

text = """ Space exploration has led to incredilbe scientific discoveries. From landing on the Moon to These missions have not only expanded our knwoledge of the universe but have also contributed to advancements in technology here on Earth. satallite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs. """


splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
)

result = splitter.split_text(text)

print(result)
print(result1[0].page_content)