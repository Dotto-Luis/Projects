# src/agent/ai_agent.py

from dataclasses import dataclass

import pandas as pd

from src.agent.openai_client import get_client
from src.utils.data_summary import create_data_summary

MODEL = "gpt-4o-mini"


@dataclass
class AgentResponse:
    """Answer plus token usage, for cost tracking."""

    answer: str
    prompt_tokens: int
    completion_tokens: int


def build_prompt(user_query: str, df: pd.DataFrame) -> str:
    """Compose the analyst prompt from the dataset summary and the question."""
    data_context = create_data_summary(df)
    return (
        "You are a data analyst AI.\n\n"
        f"Dataset summary:\n{data_context}\n"
        f"Answer this question:\n{user_query}\n\n"
        "Give only the final answer — no code, no explanations."
    )


def ai_agent(user_query: str, df: pd.DataFrame) -> AgentResponse:
    """Answer a natural-language question about the dataframe using the LLM."""
    response = get_client().chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": build_prompt(user_query, df)}],
        temperature=0,
        max_tokens=300,
    )
    return AgentResponse(
        answer=response.choices[0].message.content,
        prompt_tokens=response.usage.prompt_tokens,
        completion_tokens=response.usage.completion_tokens,
    )
