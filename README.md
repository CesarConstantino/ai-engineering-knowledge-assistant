# 🤖 AI Engineering Knowledge Assistant

Asistente inteligente basado en **RAG (Retrieval Augmented Generation)** construido con **LangGraph, LangChain y Google Gemini**.

El objetivo del proyecto es crear un sistema capaz de consultar una base de conocimiento documental utilizando inteligencia artificial generativa, recuperando información relevante desde documentos PDF antes de generar una respuesta.

---

# 📌 Descripción del Proyecto

Este proyecto implementa un asistente de conocimiento empresarial que permite realizar preguntas sobre documentos técnicos.

El flujo combina:

- Procesamiento documental.
- Generación de embeddings.
- Búsqueda semántica.
- Recuperación aumentada con contexto.
- Generación de respuestas mediante un modelo LLM.

La arquitectura implementada corresponde al patrón **RAG Architecture**.

---

# 🏗️ Arquitectura

```text
PDF Documents
      |
      v
Document Loader
(PyPDFLoader)
      |
      v
Text Splitter
      |
      v
Gemini Embeddings
      |
      v
FAISS Vector Store
      |
      v
Retriever
      |
      v
LangGraph Workflow
      |
      v
Google Gemini LLM
      |
      v
Final Answer