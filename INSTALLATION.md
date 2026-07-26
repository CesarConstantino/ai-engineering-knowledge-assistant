# ⚙️ Installation Guide

## Requirements

Before running the project, make sure you have installed:

* Python 3.12 or higher
* Git
* Google Gemini API Key

---

# 1. Clone the Repository

```bash
git clone https://github.com/CesarConstantino/ai-engineering-knowledge-assistant.git
```

Replace the URL with your repository if it has a different name.

---

# 2. Enter the Project Folder

```bash
cd ai-engineering-knowledge-assistant
```

---

# 3. Create a Virtual Environment

```bash
python -m venv .venv
```

---

# 4. Activate the Virtual Environment

## Windows

```bash
.venv\Scripts\activate
```

## Linux / macOS

```bash
source .venv/bin/activate
```

---

# 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 6. Configure Environment Variables

Create a file named `.env` in the project root.

Example:

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

---

# 7. Add Your Documents

Place one or more PDF documents inside the `data/` folder.

---

# 8. Generate the Vector Database

```bash
python ingest.py
```

This command:

* Reads the PDF files
* Splits the documents into chunks
* Generates embeddings using Google Gemini
* Stores the vectors in FAISS

---

# 9. Run the Application

```bash
python app.py
```

---

# Expected Output

```text
============================================================
🤖 AI Engineering Knowledge Assistant
============================================================

👤 Tú:
```

At this point, the assistant is ready to answer questions about the processed documents.

---

# Troubleshooting

## Missing API Key

Verify that the `.env` file exists and contains a valid `GOOGLE_API_KEY`.

---

## Module Not Found

Run:

```bash
pip install -r requirements.txt
```

again.

---

## Empty Responses

Run:

```bash
python ingest.py
```

to regenerate the FAISS vector database.
