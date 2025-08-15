from langchain_community.vectorstores import Chroma
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


from langchain_community.document_loaders import TextLoader

# Just load the document
loader=TextLoader('langchain/rag/speech.txt')
docs=loader.load()
print(docs)



#Now split the document into chunks
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
final_documents=text_splitter.split_documents(docs)

print(final_documents)

#create embeddings instance
embeddings_1024=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=1024)


#Combining vector embedding and vector store 
from langchain_community.vectorstores import Chroma 

#create a chroma db instance using the final_documents and embeddings_1024
db = Chroma.from_documents(final_documents, embeddings_1024)

#now we can query the db
query = "It will be easier for us to conduct ourselves as belligerents"
retreived_results = db.similarity_search(query)
print(retreived_results)






