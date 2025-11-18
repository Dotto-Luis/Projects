from typing import List

from langchain.schema.document import Document
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_community.vectorstores.chroma import Chroma

from backend.config import settings


def load_vector_store() -> Chroma:
    """Build a vector base on Chroma. As a embedding function, we use HuggingFaceEmbeddings"""
    print(settings.CHROMA_DB_PATH, settings.CHROMA_COLLECTION)
    return Chroma(
        persist_directory=settings.CHROMA_DB_PATH,
        collection_name=settings.CHROMA_COLLECTION,
        embedding_function=SentenceTransformerEmbeddings(
            model_name=settings.EMBEDDINGS_MODEL
        ),
    )


class Retriever:
    """Retriever class to search jobs into a Chroma vector store."""

    def __init__(self):
        self.vector_store = load_vector_store()

    def search(self, query: str, k: int = 4) -> List[Document]:
        kits = self.vector_store.similarity_search(query=query, k=k)

        return kits
