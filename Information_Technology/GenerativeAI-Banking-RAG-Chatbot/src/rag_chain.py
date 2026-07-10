from langchain.chains import RetrievalQA
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from transformers import AutoTokenizer, pipeline

from src.prompts import get_prompt_template

# flan-t5-base is a seq2seq model: CPU-friendly and compatible with the
# "text2text-generation" pipeline. Must match src/model_downloader.py.
DEFAULT_MODEL_ID = "google/flan-t5-base"
DEFAULT_EMBEDDINGS_MODEL = "all-MiniLM-L6-v2"


def build_rag_chain(
    persist_directory: str = "db/chroma/",
    model_id: str = DEFAULT_MODEL_ID,
) -> RetrievalQA:
    """
    Builds a RAG chain using a local LLM and Chroma vector DB, with a custom prompt.

    Args:
        persist_directory (str): Path to the Chroma DB.
        model_id (str): Hugging Face model ID for the LLM (seq2seq).

    Returns:
        RetrievalQA: LangChain chain ready to handle queries.
    """
    # Load vector store
    embeddings = HuggingFaceEmbeddings(model_name=DEFAULT_EMBEDDINGS_MODEL)
    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings,
    )

    # Load language model (local, CPU)
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    generator = pipeline(
        "text2text-generation",
        model=model_id,
        tokenizer=tokenizer,
        device=-1,  # CPU
    )
    llm = HuggingFacePipeline(pipeline=generator)

    # Load prompt template
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=get_prompt_template(),
    )

    # Build RAG chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(),
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=False,
    )

    return qa_chain
