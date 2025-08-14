from langchain_community.document_loaders import TextLoader


# reading text document
loader =  TextLoader('speech.txt')

text_document =  loader.load()
print(text_document)

