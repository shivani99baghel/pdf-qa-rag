# 📄 PDF Q&A System (RAG आधारित)

## 🔍 Problem
Reading large PDFs and finding answers manually is time-consuming.

## 💡 Solution
This project allows users to ask questions and get answers directly from a PDF using AI.

## ⚙️ How it Works (RAG)
1. Load PDF and extract text
2. Split text into chunks
3. Convert chunks into embeddings
4. Store embeddings in FAISS (vector DB)
5. On query:
   - Retrieve top-3 relevant chunks
   - Send context + question to LLM (Groq)
   - Generate answer

## 🧠 Tech Stack
- Python
- LangChain
- HuggingFace Embeddings
- FAISS
- Groq LLM

## ▶️ How to Run

```bash
pip install -r requirements.txt
export GROQ_API_KEY="your_key_here"
python main.py