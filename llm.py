from langchain_groq import ChatGroq

MODEL_NAME = "llama-3.1-8b-instant"

def get_llm():
    return ChatGroq(
        model=MODEL_NAME,
        temperature=0
    )

def generate_answer(llm, context, query):
    prompt = f"""
    Answer the question based ONLY on the context below.

    Context:
    {context}

    Question:
    {query}
    """
    response = llm.invoke(prompt)
    return response.content