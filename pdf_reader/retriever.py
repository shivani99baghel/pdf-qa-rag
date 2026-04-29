from langchain.text_splitter import CharacterTextSplitter

def split_text(text):
    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_text(text)

def retrieve_docs(vector_store, query, k=3):
    return vector_store.similarity_search(query, k=k)