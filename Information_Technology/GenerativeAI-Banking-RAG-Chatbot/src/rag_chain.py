from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from transformers import AutoTokenizer, pipeline
from langchain import HuggingFacePipeline
from src.prompts import get_prompt_template


def build_rag_chain(
    persist_directory: str = "db/chroma/",
    model_id: str = "stabilityai/stablelm-tuned-alpha-3b"
) -> RetrievalQA:
    """
    Builds a RAG chain using a local LLM and Chroma vector DB, with a custom prompt.

    Args:
        persist_directory (str): Path to the Chroma DB.
        model_id (str): Hugging Face model ID for the LLM.

    Returns:
        RetrievalQA: LangChain chain ready to handle queries.
    """
    try:
        # Load vector store
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectordb = Chroma(
            persist_directory=persist_directory,
            embedding_function=embeddings
        )

        # Load language model
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        generator = pipeline(
            "text-generation",
            model=model_id,
            tokenizer=tokenizer,
            trust_remote_code=True,
            device_map="auto"
        )

        llm = HuggingFacePipeline(pipeline=generator)

        # Load prompt template
        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=get_prompt_template()
        )

        # Build RAG chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vectordb.as_retriever(),
            chain_type="stuff",
            chain_type_kwargs={"prompt": prompt},
            return_source_documents=False
        )

        print("✅ RAG chain with custom prompt ready")
        return qa_chain

    except Exception as e:
        print(f"❌ Error building RAG chain: {e}")
        return None
