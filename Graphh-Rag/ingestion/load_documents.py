from langchain_community.document_loaders import TextLoader

loader = TextLoader(file_path="dummytext.txt")
docs = loader.load()
