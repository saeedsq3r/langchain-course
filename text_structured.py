# recursive character text splitting
# p--> \n\n, \n --> line, _ -->space/words, '' --> character
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """ Space exploration has led to incredilbe scientific discoveries. From landing on the Moon to These missions have not only expanded our knwoledge of the universe but have also contributed to advancements in technology here on Earth. satallite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs. """

# Perform the split
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)

