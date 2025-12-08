from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_experimental.llms import OllamaFunctions  


class Entities(BaseModel):
    """Identifying information about entities."""

    names: list[str] = Field(
        ...,
        description="All the person, organization, or business entities that "
        "appear in the text",
    )

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are extracting organization and person entities from the text.",
        ),
        (
            "human",
            "Use the given format to extract information from the following "
            "input: {question}",
        ),
    ]
)

llm = OllamaFunctions(model="llama3.1:8b", temperature=0, format="json", base_url="http://ollama:11434")
entity_chain = llm.with_structured_output(Entities)

entity_chain.invoke("Who are Nonna Lucia and Giovanni Caruso?")