from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

from config import GOOGLE_API_KEY


VECTOR_STORE_PATH = "vector_store"


print("Cargando FAISS...")


embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=GOOGLE_API_KEY
)


vector_store = FAISS.load_local(
    VECTOR_STORE_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)


print("FAISS cargado correctamente")


retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 4
    }
)


def search_documents(question: str) -> str:

    documents = retriever.invoke(question)

    context = "\n\n".join(
        [
            doc.page_content
            for doc in documents
        ]
    )

    return context