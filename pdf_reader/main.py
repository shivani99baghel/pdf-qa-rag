from pdf_loader import load_pdf
from retriever import split_text, retrieve_docs
from embeddings import create_vector_store
from llm import get_llm, generate_answer

def main():
    pdf_path = "/Users/admin/Documents/Shivani-Baghel-Resume-AI.pdf"

    print("Loading PDF...")
    text = load_pdf(pdf_path)

    print("Splitting text...")
    chunks = split_text(text)

    print("Creating embeddings...")
    vector_store = create_vector_store(chunks)

    llm = get_llm()

    print("\n✅ Ready! Ask questions (type 'exit' to quit)\n")

    while True:
        query = input("Ask: ")

        if query.lower() == "exit":
            break

        docs = retrieve_docs(vector_store, query, k=3)
        context = "\n".join([doc.page_content for doc in docs])

        answer = generate_answer(llm, context, query)

        print("\n--- Answer ---")
        print(answer)
        print("--------------\n")


if __name__ == "__main__":
    main()