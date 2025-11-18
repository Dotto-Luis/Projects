from typing import List, Optional

import pandas as pd
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_community.vectorstores.chroma import Chroma
from tqdm import tqdm

from backend.config import settings


class ETLProcessor:
    """
    This class is responsible for performing an Extract-Transform-Load (ETL)
    process for document embedding.
    """

    def __init__(
        self,
        batch_size: int,
        chunk_size: int,
        chunk_overlap: int,
        dataset_path: Optional[str] = settings.DATASET_PATH,
        embedding_model: Optional[str] = settings.EMBEDDINGS_MODEL,
        collection_name: Optional[str] = settings.CHROMA_COLLECTION,
        persist_directory: Optional[str] = settings.CHROMA_DB_PATH,
    ):
        """
        Initializes the ETLProcessor object with a specified batch_size.

        Parameters
        ----------
        batch_size : int
            Number of documents to process in each batch, e.g. 100.

        chunk_size : int
            Size of chunks to be split into, e.g. 500.

        chunk_overlap : int
            Number of characters to overlap between chunks, e.g. 20.

        dataset_path : str, optional
            Path to csv file containing the dataset.

        embedding_model : str, optional
            Name of the embedding model to be used, e.g.
            "paraphrase-MiniLM-L6-v2".

        collection_name : str, optional
            Name of the collection to be used in the vector store.

        persist_directory : str, optional
            Directory to persist the vector store.
        """
        self.dataset_path = dataset_path
        self.batch_size = batch_size
        self.embedding = SentenceTransformerEmbeddings(
            model_name=embedding_model
        )
        self.collection_name = collection_name
        self.persist_directory = persist_directory

        # TODO: Create a text splitter using the
        # `langchain.text_splitter.RecursiveCharacterTextSplitter` class.
        # Hint: Use the `chunk_size` and `chunk_overlap` parameters.


    def load_data(self) -> pd.DataFrame:
        """
        Loads the jobs descriptions from a csv file.

        Returns
        -------
        df : pd.DataFrame
            Jobs descriptions with extra metadata from the dataset.
        """
        # TODO: Load the dataset from the `dataset_path` using the
        # `pandas.read_csv()` function.
        # Keep only the following columns: "description", "Employment type",
        # "Seniority level", "company", "location", "post_url", "title".
        # Discard the rest.
        # Drop the entire row if any nan values are found on some of the
        # chosen columns.
        

    def create_documents(self, descriptions: pd.DataFrame) -> List[Document]:
        """
        Creates a list of Document objects from given descriptions.

        Parameters
        ----------
        descriptions : pd.DataFrame
            Job descriptions to be converted to Document objects.

        Returns
        -------
        List[Document]
            List of Document (langchain.docstore.document.Document) objects.
        """
        output_documents = []
        for idx, row in descriptions.iterrows():
            metadata = {
                "employment_type": row["Employment type"],
                "seniority_level": row["Seniority level"],
                "company": row["company"],
                "location": row["location"],
                "post_url": row["post_url"],
                "title": row["title"],
                "id": idx,
            }
            doc = Document(page_content=row["description"], metadata=metadata)
            output_documents.append(doc)

        return output_documents

    def split_documents(self, documents: List[Document]) -> List[Document]:
        """
        Splits documents into smaller chunks using the pre-defined
        text_splitter.

        Parameters
        ----------
        documents : List[Document]
            List of Document objects to be split.

        Returns
        -------
        List[Document]
            List of split Document objects.
        """
        return self.text_splitter.split_documents(documents)

    def process_batches(self, splits: List[Document]) -> None:
        """
        Processes documents in batches, creating Chroma vector stores for
        each batch.

        Parameters
        ----------
        splits : List[Document]
            List of Document objects to be processed.

        Returns
        -------
        None
        """
        for i in tqdm(
            range(0, len(splits), self.batch_size), desc="Processing batches"
        ):
            Chroma.from_documents(
                splits[i: i + self.batch_size],
                embedding=self.embedding,
                collection_name=self.collection_name,
                persist_directory=self.persist_directory,
            )

    def run_etl(self) -> None:
        """
        Executes the ETL process: extract data from a source, transform it,
        and load into a new storage.
        """
        job_descriptions = self.load_data()
        docs = self.create_documents(job_descriptions)[:100]
        splits = self.split_documents(docs)
        self.process_batches(splits)


if __name__ == "__main__":
    etl_processor = ETLProcessor(
        batch_size=32,
        chunk_size=500,
        chunk_overlap=100,
    )
    etl_processor.run_etl()
