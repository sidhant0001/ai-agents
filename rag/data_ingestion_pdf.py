from langchain_community.document_loaders import PyPDFLoader


# reading text document
loader =  PyPDFLoader('attention.pdf')

pdf_document =  loader.load()
print(pdf_document)