from typing import List, Optional

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings


def embed_and_store_documents(
    chunks: List[Document],
    persist_directory: str = "db/chroma/",
    model_name: str = "all-MiniLM-L6-v2",
) -> Optional[Chroma]:
    """
    Vectorizes text chunks and stores them in a Chroma vector database.

    Args:
        chunks (List[Document]): List of LangChain Document chunks.
        persist_directory (str): Directory to save Chroma DB.
        model_name (str): Hugging Face embedding model to use.

    Returns:
        Chroma: The vector store object ready for retrieval.
    """
    embedding_model = HuggingFaceEmbeddings(model_name=model_name)
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
    )
    return vectorstore
