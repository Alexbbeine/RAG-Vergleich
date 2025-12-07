from langchain_text_splitters import RecursiveCharacterTextSplitter
from ingestion.load_documents import docs

text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=24)
documents = text_splitter.split_documents(documents=docs)
