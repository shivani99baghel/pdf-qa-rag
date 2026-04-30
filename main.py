from dotenv import load_dotenv
import os

load_dotenv()

# optional check
print("Key loaded:", bool(os.getenv("GROQ_API_KEY")))

from pdf_loader import load_pdf_with_pages
from retriever import split_text_with_metadata, retrieve_docs
from embeddings import create_vector_store
from llm import get_llm, generate_answer

def main():
    pdf_path = "/Users/admin/Documents/Shivani-Baghel-Resume-AI.pdf"

    print("📄 Loading PDF...")
    docs = load_pdf_with_pages(pdf_path)

    print("✂️ Splitting text...")
    chunks = split_text_with_metadata(docs)

    print("🧠 Creating embeddings...")
    vector_store = create_vector_store(chunks)

    llm = get_llm()

    print("\n✅ Ready! Ask questions (type 'exit' to quit)\n")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            break

        docs = retrieve_docs(vector_store, query, k=4)

        context = "\n".join([doc.page_content for doc in docs])
        answer = generate_answer(llm, context, query)

        print("\n🤖 AI:", answer)

        print("\n📌 Sources:")
        for i, doc in enumerate(docs):
            page = doc.metadata.get("page", "N/A")
            snippet = doc.page_content[:150].replace("\n", " ")
            print(f"{i+1}. Page {page}: {snippet}...")

        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    main()