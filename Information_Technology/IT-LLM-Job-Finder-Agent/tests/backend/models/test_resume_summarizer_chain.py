from unittest.mock import MagicMock, patch

from backend.config import settings
from backend.models.resume_summarizer_chain import get_resume_summarizer_chain, template


@patch("backend.models.resume_summarizer_chain.PromptTemplate")
@patch("backend.models.resume_summarizer_chain.get_llm")
@patch("backend.models.resume_summarizer_chain.LLMChain")
def test_get_resume_summarizer_chain(
    LLMChainMock, get_llm_mock, PromptTemplateMock
):
    # Mock the PromptTemplate class
    prompt_mock = MagicMock()
    PromptTemplateMock.return_value = prompt_mock

    # Mock the get_llm function
    llm_mock = MagicMock()
    get_llm_mock.return_value = llm_mock

    # Create an instance of the LLMChain class
    llm_chain_mock = MagicMock()
    LLMChainMock.return_value = llm_chain_mock

    # Call the get_resume_summarizer_chain function
    resume_summarizer_chain = get_resume_summarizer_chain()

    # Assert that the PromptTemplate class was called with the correct arguments
    PromptTemplateMock.assert_called_once_with(
        input_variables=["resume"], template=template
    )

    # Assert that the get_llm function was called with the correct arguments
    get_llm_mock.assert_called_once_with(
        temperature=0,
        provider=settings.LLM_PROVIDER
    )

    # Assert that the LLMChain class was called with the correct arguments
    LLMChainMock.assert_called_once_with(
        llm=llm_mock, prompt=prompt_mock, verbose=settings.LANGCHAIN_VERBOSE
    )

    # Assert that the get_resume_summarizer_chain function returns the expected result
    assert resume_summarizer_chain == llm_chain_mock