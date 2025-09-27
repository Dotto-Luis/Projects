# src/agent/ai_agent.py

from src.agent.openai_client import client
from src.utils.data_summary import create_data_summary

def ai_agent(user_query, df):
    data_context = create_data_summary(df)

    prompt = f"""
You are a data expert AI agent.

You have been provided with this dataset summary:
{data_context}

Now, based on the user's question:
'{user_query}'

Think step-by-step. Assume you can access and analyze the dataset like a Data Scientist would using Pandas.

Give a clear, final answer.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=500
    )

    return response.choices[0].message.content
