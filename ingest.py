import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

from config import GOOGLE_API_KEY


DATA_PATH = "data"
VECTOR_STORE_PATH = "vector_store"


def load_documents():

    documents = []

    for file in os.listdir(DATA_PATH):

        if file.endswith(".pdf"):

            path = os.path.join(
                DATA_PATH,
                file
            )

            print(f"📄 Leyendo: {file}")

            loader = PyPDFLoader(path)

            documents.extend(
                loader.load()
            )

    return documents



def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    return splitter.split_documents(
        documents
    )



def create_vector_store(chunks):

    print("🧠 Creando embeddings...")


    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=GOOGLE_API_KEY
    )


    print("🔎 Creando índice FAISS...")


    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )


    print("💾 Guardando vector store...")


    vector_store.save_local(
        VECTOR_STORE_PATH
    )


    print("✅ FAISS guardado correctamente")



def main():

    print("📄 Cargando documentos...")


    documents = load_documents()


    if not documents:

        print("❌ No hay documentos PDF en data/")

        return


    print(
        f"Documentos encontrados: {len(documents)}"
    )


    print("✂️ Dividiendo documentos...")


    chunks = split_documents(
        documents
    )


    print(
        f"Fragmentos creados: {len(chunks)}"
    )


    create_vector_store(
        chunks
    )


    print(
        "🚀 Proceso terminado"
    )



if __name__ == "__main__":

    main()