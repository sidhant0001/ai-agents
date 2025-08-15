import os
from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEmbeddings

os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")



embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

text="this is atest documents"
query_result=embeddings.embed_query(text)
print(query_result)

doc_result = embeddings.embed_documents([text, "This is not a test document."])
doc_result[0]

