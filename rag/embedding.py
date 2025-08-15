import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import OpenAIEmbeddings

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

embeddings_1024 = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1024)


text = "1982 Honda goldwing"
query_Result = embeddings_1024.embed_query(text)
print(len(query_Result))


from langchain_community.document_loaders import TextLoader


# reading text document
loader =  TextLoader('langchain/rag/speech.txt')

docs  =  loader.load()
print(docs)

from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
final_document = text_splitter.split_documents(docs)
print(final_document)





