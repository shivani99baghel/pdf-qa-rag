from langchain.text_splitter import CharacterTextSplitter

def split_text_with_metadata(docs):
    splitter = CharacterTextSplitter(
        chunk_size=700,   # improved
        chunk_overlap=100
    )

    chunks = []

    for doc in docs:
        splits = splitter.split_text(doc["text"])
        for chunk in splits:
            chunks.append({
                "text": chunk,
                "metadata": {"page": doc["page"]}
            })

    return chunks


def retrieve_docs(vector_store, query, k=4):
    return vector_store.similarity_search(query, k=k)