from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_store(chunks_with_metadata):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    texts = [item["text"] for item in chunks_with_metadata]
    metadatas = [item["metadata"] for item in chunks_with_metadata]

    return FAISS.from_texts(texts, embeddings, metadatas=metadatas)