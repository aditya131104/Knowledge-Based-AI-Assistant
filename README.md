# 🤖 Knowledge-Based AI Assistant

A PDF-based question answering system built using **Retrieval-Augmented Generation (RAG)**. The application retrieves relevant information from a document and uses **Google Gemini** to generate answers from the retrieved context.

## 🔄 RAG Workflow

**PDF → Text Extraction → Chunking → Embeddings → FAISS → User Query → Similarity Search → Top-K Chunks → Gemini → Answer**

## 🧠 How It Works

1. **Text Extraction** – Extracts text from the PDF using PyPDF.
2. **Chunking** – Splits the extracted text into smaller chunks using RecursiveCharacterTextSplitter.
3. **Embeddings** – Converts document chunks into vector representations using Gemini Embeddings.
4. **Retrieval** – FAISS performs similarity search and retrieves the top 3 relevant chunks for the user's question.
5. **Generation** – The retrieved chunks and question are provided to Google Gemini as context.
6. **Response** – Gemini generates the final answer, which is displayed through Streamlit.

## 🛠️ Tech Stack

**Python · LangChain · Google Gemini · FAISS · PyPDF · Streamlit**

## ✨ Features

- PDF-based question answering
- Semantic similarity search
- Top-K relevant context retrieval
- Gemini-powered answer generation
- Streamlit web interface
- Persistent FAISS vector index

## 🔮 Future Improvements

- PDF upload through the UI
- Multiple document support
- Source/page citations
- OCR for scanned PDFs
- Hybrid search

## 👨‍💻 Author

**Aditya Raj**  
B.Tech CSE (Data Science)
