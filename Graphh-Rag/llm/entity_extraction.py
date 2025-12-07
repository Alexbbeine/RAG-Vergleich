from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from llm.llm_setup import llm

class Entities(BaseModel):
    names: list[str] = Field(
        ...,
        description="All the person, organization, or business entities that appear in the text",
    )

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are extracting organization and person entities from the text."),
        ("human", "Use the given format to extract information from the following input: {question}"),
    ]
)

entity_chain = llm.with_structured_output(Entities)
