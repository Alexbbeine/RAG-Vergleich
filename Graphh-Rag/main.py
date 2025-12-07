from llm.answer_chain import chain

print(
    chain.invoke(
        input="Who is Nonna Lucia? Did she teach anyone about restaurants or cooking?"
    )
)
