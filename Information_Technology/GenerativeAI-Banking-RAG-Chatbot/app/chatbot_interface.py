"""Command-line interface for the banking RAG chatbot.

Usage:
    python -m app.chatbot_interface ingest data/Spain_unicaja_Fixed_Mortage.pdf
    python -m app.chatbot_interface chat
"""

import argparse

from langchain_core.documents import Document

from src.embeddings import embed_and_store_documents
from src.loader import ocr_pdf_to_text_chunks
from src.rag_chain import build_rag_chain

DB_DIR = "db/chroma/"


def ingest(pdf_path: str) -> None:
    """OCR a PDF, chunk it, and store embeddings in the vector DB."""
    chunks = ocr_pdf_to_text_chunks(pdf_path)
    documents = [Document(page_content=chunk) for chunk in chunks]
    embed_and_store_documents(documents, persist_directory=DB_DIR)
    print(f"Ingested {len(documents)} chunks from {pdf_path} into {DB_DIR}")


def chat() -> None:
    """Interactive Q&A loop over the ingested documents."""
    qa_chain = build_rag_chain(persist_directory=DB_DIR)
    print("Banking RAG chatbot ready. Type 'exit' to quit.")
    while True:
        question = input("\nYou: ").strip()
        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue
        result = qa_chain.invoke({"query": question})
        print(f"\nBot: {result['result']}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Banking RAG chatbot")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest_parser = subparsers.add_parser("ingest", help="Ingest a PDF into the vector DB")
    ingest_parser.add_argument("pdf_path", help="Path to the PDF file")

    subparsers.add_parser("chat", help="Start an interactive chat session")

    args = parser.parse_args()
    if args.command == "ingest":
        ingest(args.pdf_path)
    elif args.command == "chat":
        chat()


if __name__ == "__main__":
    main()
