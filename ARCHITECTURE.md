# 🏗️ System Architecture

## Overview

AI Engineering Knowledge Assistant implements a **Retrieval-Augmented Generation (RAG)** architecture.

Instead of relying only on the Large Language Model (LLM), the application first retrieves the most relevant information from a knowledge base and then uses that context to generate accurate answers.

This approach reduces hallucinations and allows the assistant to answer questions using the information contained in enterprise documents.

---

# High-Level Architecture

```text
                    User Question
                          │
                          ▼
                    LangGraph Workflow
                          │
                          ▼
                      Retriever
                          │
                          ▼
                  FAISS Vector Store
                          ▲
                          │
              Google Gemini Embeddings
                          ▲
                          │
       RecursiveCharacterTextSplitter
                          ▲
                          │
                  PyPDFLoader
                          ▲
                          │
                     PDF Documents
```

---

# Processing Flow

## 1. Document Loading

The application reads PDF files stored inside the **data/** directory using **PyPDFLoader**.

---

## 2. Document Splitting

Documents are divided into smaller chunks using **RecursiveCharacterTextSplitter**.

Current configuration:

* Chunk Size: 1000
* Chunk Overlap: 200

This improves semantic retrieval accuracy.

---

## 3. Embedding Generation

Each chunk is converted into a semantic vector using:

* Google Gemini Embeddings
* Model: `models/gemini-embedding-001`

---

## 4. Vector Storage

Embeddings are stored inside a **FAISS Vector Database**, allowing fast similarity search.

---

## 5. Semantic Retrieval

When the user asks a question:

1. The question is converted into an embedding.
2. FAISS searches for the most similar document chunks.
3. The retrieved context is returned to the application.

---

## 6. Context Augmentation

The retrieved context is combined with:

* System Prompt
* User Question
* Conversation History

This information is sent to the Large Language Model.

---

## 7. Response Generation

The final response is generated using:

* Google Gemini 3.1 Flash Lite

The answer is based on both:

* Retrieved document context
* User question

---

# Main Components

| Component                      | Responsibility               |
| ------------------------------ | ---------------------------- |
| PyPDFLoader                    | Reads PDF documents          |
| RecursiveCharacterTextSplitter | Splits documents into chunks |
| Google Gemini Embeddings       | Generates semantic vectors   |
| FAISS                          | Stores embeddings            |
| Retriever                      | Finds relevant information   |
| LangGraph                      | Orchestrates the workflow    |
| Google Gemini                  | Generates the final response |

---

# Project Architecture

```text
src/
│
├── graph.py
│      LangGraph workflow
│
├── llm.py
│      Gemini integration
│
├── retriever.py
│      FAISS retrieval
│
├── memory.py
│      Conversation memory
│
├── tools.py
│      Tool definitions
│
└── prompts/
       template.py
       System Prompt
```

---

# Design Principles

The project follows the following engineering principles:

* Modular architecture
* Separation of responsibilities
* Retrieval-Augmented Generation (RAG)
* Reusable components
* Easy maintainability
* Scalable design

---

# Future Improvements

* Multi-document ingestion
* Metadata filtering
* Hybrid Search
* Streaming responses
* Web interface with Streamlit
* Persistent conversation memory
* OCI production deployment
