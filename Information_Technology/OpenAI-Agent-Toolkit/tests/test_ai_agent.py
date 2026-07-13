from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src.agent.ai_agent import MODEL, ai_agent, build_prompt
from src.agent.openai_client import get_client


@pytest.fixture
def df():
    return pd.DataFrame({"Loan_ID": ["LP1", "LP2"], "LoanAmount": [100, 200]})


def test_build_prompt_contains_summary_and_question(df):
    prompt = build_prompt("How many loans are there?", df)

    assert "How many loans are there?" in prompt
    assert "2 rows and 2 columns" in prompt
    assert "Loan_ID" in prompt


@patch("src.agent.ai_agent.get_client")
def test_ai_agent_calls_llm_and_returns_answer(get_client_mock, df):
    """The agent sends the composed prompt to the LLM and returns answer + usage."""
    completion = MagicMock()
    completion.choices[0].message.content = "There are 2 loans."
    completion.usage.prompt_tokens = 120
    completion.usage.completion_tokens = 8
    get_client_mock.return_value.chat.completions.create.return_value = completion

    result = ai_agent("How many loans are there?", df)

    assert result.answer == "There are 2 loans."
    assert result.prompt_tokens == 120
    assert result.completion_tokens == 8
    call_kwargs = get_client_mock.return_value.chat.completions.create.call_args.kwargs
    assert call_kwargs["model"] == MODEL
    assert call_kwargs["temperature"] == 0
    assert "How many loans are there?" in call_kwargs["messages"][0]["content"]


def test_get_client_requires_api_key(monkeypatch):
    """Client creation fails fast with a clear error when the key is missing."""
    get_client.cache_clear()
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setattr("src.agent.openai_client.load_dotenv", lambda: None)

    with pytest.raises(RuntimeError, match="OPENAI_API_KEY"):
        get_client()

    get_client.cache_clear()
