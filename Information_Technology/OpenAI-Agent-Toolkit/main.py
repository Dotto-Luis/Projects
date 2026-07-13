# main.py

import sys

from openai import AuthenticationError, OpenAIError

from src.agent.ai_agent import ai_agent
from src.utils.data_loader import load_loan_data

# gpt-4o-mini pricing per 1M tokens (USD) — check openai.com/pricing for updates
PRICE_INPUT = 0.15
PRICE_OUTPUT = 0.60

print("Welcome to Loan Review AI Agent!")
print("You can ask anything about the loan applicants data.")
print("Type 'exit' to quit.\n")

df = load_loan_data()
total_cost = 0.0

while True:
    user_input = input("Your question: ").strip()
    if user_input.lower() in {"exit", "quit"}:
        print(f"Goodbye! Session total: ${total_cost:.5f}")
        break
    if not user_input:
        continue

    try:
        result = ai_agent(user_input, df)
    except AuthenticationError:
        sys.exit(
            "\nError: invalid OpenAI API key. "
            "Edit .env and set a valid OPENAI_API_KEY "
            "(https://platform.openai.com/api-keys)."
        )
    except OpenAIError as e:
        print(f"\nOpenAI API error: {e}\n")
        continue

    cost = (
        result.prompt_tokens * PRICE_INPUT + result.completion_tokens * PRICE_OUTPUT
    ) / 1_000_000
    total_cost += cost

    print("\nAI Agent Response:\n")
    print(result.answer)
    print(
        f"\n[tokens: {result.prompt_tokens} in / {result.completion_tokens} out"
        f" · cost: ${cost:.5f} · session: ${total_cost:.5f}]\n"
    )
