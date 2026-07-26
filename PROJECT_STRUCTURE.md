# 📂 Project Structure

## Overview

This document describes the organization of the **AI Engineering Knowledge Assistant** repository.

The project follows a modular architecture where each component has a specific responsibility, allowing easier maintenance, scalability and future extensions.

---

# Repository Structure

```text
ai-engineering-knowledge-assistant/
│
├── data/
│   │
│   └── PDF Documents
│
├── vector_store/
│   │
│   └── FAISS Index
│
├── src/
│   │
│   ├── graph.py
│   │       LangGraph workflow definition
│   │
│   ├── llm.py
│   │       Google Gemini integration
│   │
│   ├── retriever.py
│   │       Semantic search and document retrieval
│   │
│   ├── memory.py
│   │       Conversation memory management
│   │
│   ├── tools.py
│   │       Custom agent tools
│   │
│   ├── models/
│   │       Model configurations
│   │
│   └── prompts/
│           System prompts and templates
│
├── app.py
│       Main application entry point
│
├── ingest.py
│       Document ingestion and FAISS generation process
│
├── config.py
│       Environment configuration management
│
├── requirements.txt
│       Project dependencies
│
├── README.md
│       Main project documentation
│
├── ARCHITECTURE.md
│       System architecture documentation
│
├── INSTALLATION.md
│       Installation guide
│
└── PROJECT_STRUCTURE.md
        Repository organization documentation
```

---

# Main Components

## app.py

Application entry point.

Responsibilities:

* Receive user questions.
* Execute the LangGraph workflow.
* Display generated responses.

---

## ingest.py

Responsible for preparing the knowledge base.

Process:

1. Load PDF documents.
2. Split documents into chunks.
3. Generate embeddings.
4. Create FAISS vector database.

---

## src/graph.py

Defines the agent workflow using LangGraph.

Responsibilities:

* Manage execution flow.
* Connect retrieval and generation steps.
* Control state transitions.

---

## src/retriever.py

Responsible for information retrieval.

Responsibilities:

* Load FAISS vector database.
* Search relevant document fragments.
* Provide context to the LLM.

---

## src/llm.py

Handles communication with Google Gemini.

Responsibilities:

* Configure the language model.
* Send prompts.
* Generate responses.

---

## src/prompts/

Contains the prompts used by the assistant.

Responsibilities:

* Define system behavior.
* Establish AI role and response guidelines.

---

## src/memory.py

Manages conversation history.

Allows the assistant to maintain context during interactions.

---

# Data Flow

```text
PDF
 |
 v
ingest.py
 |
 v
FAISS Vector Store
 |
 v
retriever.py
 |
 v
graph.py
 |
 v
llm.py
 |
 v
Gemini Response
```

---

# Design Benefits

This structure provides:

* Clear separation of responsibilities.
* Easier debugging.
* Better maintainability.
* Scalability for future AI agents.
* Reusable architecture patterns.
