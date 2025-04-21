from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

def load_and_split_pdf(
    pdf_path: str,
    chunk_size: int = 500,
    chunk_overlap: int = 50
) -> List:
    """
    Loads a PDF file and splits its content into text chunks.

    Args:
        pdf_path (str): Full or relative path to the PDF file.
        chunk_size (int): Number of characters per chunk.
        chunk_overlap (int): Number of overlapping characters between chunks.

    Returns:
        List[Document]: List of text chunks (LangChain Document objects).
    """
    try:
        loader = PyPDFLoader(pdf_path)
        pages = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        chunks = splitter.split_documents(pages)
        print(f"✅ Loaded {len(pages)} pages and split into {len(chunks)} chunks.")
        return chunks

    except Exception as e:
        print(f"❌ Error loading or splitting PDF: {e}")
        return []
