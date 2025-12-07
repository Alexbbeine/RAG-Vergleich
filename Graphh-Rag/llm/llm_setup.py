from langchain_experimental.llms.ollama_functions import OllamaFunctions

llm = OllamaFunctions(
    model="llama3.1:8b",
    temperature=0,
    format="json",
    base_url="http://ollama:11434"
)
