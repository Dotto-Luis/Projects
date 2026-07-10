from unittest.mock import MagicMock, patch

from langchain_core.documents import Document

from src.embeddings import embed_and_store_documents


@patch("src.embeddings.Chroma")
@patch("src.embeddings.HuggingFaceEmbeddings")
def test_embed_and_store_documents(embeddings_mock, chroma_mock):
    """Chunks are embedded and persisted in Chroma with the right arguments."""
    embeddings_mock.return_value = MagicMock()
    chroma_mock.from_documents.return_value = MagicMock()

    chunks = [Document(page_content="chunk one"), Document(page_content="chunk two")]
    vectorstore = embed_and_store_documents(
        chunks, persist_directory="some/dir", model_name="test-model"
    )

    embeddings_mock.assert_called_once_with(model_name="test-model")
    chroma_mock.from_documents.assert_called_once_with(
        documents=chunks,
        embedding=embeddings_mock.return_value,
        persist_directory="some/dir",
    )
    assert vectorstore is chroma_mock.from_documents.return_value
