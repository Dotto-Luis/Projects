from unittest.mock import MagicMock, patch

import pandas as pd

from backend.etl import ETLProcessor


@patch("backend.etl.Chroma.from_documents")
@patch("backend.etl.SentenceTransformerEmbeddings")
@patch("backend.etl.RecursiveCharacterTextSplitter")
@patch("backend.etl.pd.read_csv")
def test_run_etl(
    pd_read_csv_mock,
    text_splitter_mock,
    sentence_transformer_mock,
    chroma_mock,
):
    # Mock the necessary dependencies
    pd_read_csv_mock.return_value = pd.DataFrame(
        {
            "description": ["description 1", "description 2"],
            "Employment type": ["type 1", "type 2"],
            "Seniority level": ["level 1", "level 2"],
            "company": ["company 1", "company 2"],
            "location": ["location 1", "location 2"],
            "post_url": ["url 1", "url 2"],
            "title": ["title 1", "title 2"],
        }
    )
    text_splitter_mock.return_value.split_documents.return_value = [
        MagicMock(),
        MagicMock(),
    ]

    # Create an instance of ETLProcessor
    etl_processor = ETLProcessor(
        batch_size=32,
        chunk_size=500,
        chunk_overlap=100,
        dataset_path="test_dataset.csv",
        embedding_model="test_model",
        collection_name="test_collection",
        persist_directory="test_directory",
    )

    # Run the ETL process
    etl_processor.run_etl()

    # Assert that the necessary methods were called with the correct arguments
    pd_read_csv_mock.assert_called_once_with("test_dataset.csv")
    text_splitter_mock.assert_called_once_with(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    sentence_transformer_mock.assert_called_once_with(model_name="test_model")
    chroma_mock.assert_called_once_with(
        text_splitter_mock.return_value.split_documents.return_value,
        embedding=sentence_transformer_mock.return_value,
        collection_name="test_collection",
        persist_directory="test_directory",
    )
