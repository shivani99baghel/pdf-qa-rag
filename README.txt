# 📄 PDF Q&A System (RAG-Based)

## 🔍 Problem Statement

Reading large PDF documents and manually searching for specific information is time-consuming and inefficient. Traditional keyword search often fails to capture semantic meaning, leading to poor results.

---

## 💡 Solution

This project builds a **PDF Question-Answering system** using a **RAG (Retrieval-Augmented Generation)** approach.

Instead of relying only on an LLM, the system:

* Retrieves relevant content from the PDF
* Uses that context to generate accurate answers

👉 This reduces hallucination and improves answer reliability.

---

## 🧠 How RAG Works (Simple Explanation)

1. Extract text from PDF
2. Break text into smaller chunks
3. Convert chunks into embeddings (numerical meaning)
4. Store embeddings in a vector database
5. On user query:

   * Find most relevant chunks (semantic search)
   * Send them to LLM
   * Generate answer based on context

---

## ⚙️ Architecture Flow

```
PDF → Chunking → Embeddings → FAISS → Retrieval → LLM → Answer
```

---

## 🛠️ Tech Stack

* Python
* LangChain
* FAISS (Vector Database)
* Groq (LLM Inference)
* HuggingFace Embeddings
* pdfplumber

---

## 💬 Sample Interaction

```
You: What is the document about?

AI: The document explains the fundamentals of machine learning, including supervised and unsupervised learning techniques.

Source:
1. Page 2: "Machine learning is a method of data analysis..."
2. Page 5: "Supervised learning involves labeled datasets..."
```

---

## 🔐 Environment Setup

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## ✨ Key Features

* ✅ Ask questions from any PDF
* ✅ Semantic search (not keyword-based)
* ✅ Source attribution (page + snippet)
* ✅ Local embeddings (no cost)
* ✅ Clean CLI interaction

---

## 🚀 Future Improvements

* Add Streamlit UI
* Support multiple PDFs
* Highlight exact answer spans
* Add confidence scoring

---

## 📌 Why This Project Matters

This project demonstrates:

* Understanding of RAG pipelines
* Handling real-world LLM limitations
* Working with embeddings + vector databases
* Building end-to-end AI systems

---

## 📬 Contact

Feel free to connect or reach out for feedback!
