from unittest.mock import MagicMock, patch

from src.prompts import get_prompt_template
from src.rag_chain import DEFAULT_MODEL_ID, build_rag_chain


def test_prompt_template_has_required_placeholders():
    template = get_prompt_template()
    assert "{context}" in template
    assert "{question}" in template


@patch("src.rag_chain.RetrievalQA")
@patch("src.rag_chain.HuggingFacePipeline")
@patch("src.rag_chain.pipeline")
@patch("src.rag_chain.AutoTokenizer")
@patch("src.rag_chain.Chroma")
@patch("src.rag_chain.HuggingFaceEmbeddings")
def test_build_rag_chain(
    embeddings_mock,
    chroma_mock,
    tokenizer_mock,
    pipeline_mock,
    hf_pipeline_mock,
    retrievalqa_mock,
):
    """The chain wires vector store, local LLM and custom prompt together."""
    retrievalqa_mock.from_chain_type.return_value = MagicMock()

    chain = build_rag_chain(persist_directory="some/db")

    # Vector store loaded from the given directory
    chroma_mock.assert_called_once()
    assert chroma_mock.call_args.kwargs["persist_directory"] == "some/db"

    # Local seq2seq model on CPU (must match model_downloader.py)
    pipeline_mock.assert_called_once()
    assert pipeline_mock.call_args.args[0] == "text2text-generation"
    assert pipeline_mock.call_args.kwargs["model"] == DEFAULT_MODEL_ID
    assert pipeline_mock.call_args.kwargs["device"] == -1

    # Chain built with the custom prompt
    build_kwargs = retrievalqa_mock.from_chain_type.call_args.kwargs
    prompt = build_kwargs["chain_type_kwargs"]["prompt"]
    assert set(prompt.input_variables) == {"context", "question"}
    assert chain is retrievalqa_mock.from_chain_type.return_value
