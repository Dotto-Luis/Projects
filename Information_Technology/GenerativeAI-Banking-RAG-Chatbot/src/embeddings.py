from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from typing import List
from langchain.schema import Document

def embed_and_store_documents(
    chunks: List[Document],
    persist_directory: str = "db/chroma/",
    model_name: str = "all-MiniLM-L6-v2"
) -> Chroma:
    """
    Vectorizes text chunks and stores them in a Chroma vector database.

    Args:
        chunks (List[Document]): List of LangChain Document chunks.
        persist_directory (str): Directory to save Chroma DB.
        model_name (str): Hugging Face embedding model to use.

    Returns:
        Chroma: The vector store object ready for retrieval.
    """
    try:
        embedding_model = HuggingFaceEmbeddings(model_name=model_name)
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            persist_directory=persist_directory
        )
        vectorstore.persist()
        print(f"✅ Chroma DB created and saved in '{persist_directory}'")
        return vectorstore

    except Exception as e:
        print(f"❌ Error creating vector store: {e}")
        return None
