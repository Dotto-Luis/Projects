from unittest.mock import MagicMock, patch

from backend.retriever import Retriever


@patch("backend.retriever.load_vector_store")
def test_retriever_search(load_vector_store_mock):
    # Mock the vector store
    vector_store_mock = MagicMock()
    load_vector_store_mock.return_value = vector_store_mock

    # Create an instance of the Retriever class
    retriever = Retriever()

    # Mock the similarity_search method of the vector store
    vector_store_mock.similarity_search.return_value = [
        "document1",
        "document2",
        "document3",
    ]

    # Call the search method of the Retriever class
    results = retriever.search("query", k=3)

    # Assert that the similarity_search method was called with the correct arguments
    vector_store_mock.similarity_search.assert_called_once_with(
        query="query", k=3
    )

    # Assert that the search method returns the expected results
    assert results == ["document1", "document2", "document3"]
