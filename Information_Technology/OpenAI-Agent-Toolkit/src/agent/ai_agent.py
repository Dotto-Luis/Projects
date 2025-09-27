# src/agent/ai_agent.py

from src.agent.openai_client import client
from src.utils.data_summary import create_data_summary

def ai_agent(user_query, df):
    data_context = create_data_summary(df)

    prompt = f"""
You are a data analyst AI.

Dataset summary:
{data_context}

Answer this question:
{user_query}

Give only the final answer — no code, no explanations.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=300
    )

    return response.choices[0].message.content
