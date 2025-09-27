# main.py

from src.utils.data_loader import load_loan_data
from src.agent.ai_agent import ai_agent

print("Welcome to Loan Review AI Agent!")
print("You can ask anything about the loan applicants data.")
print("Type 'exit' to quit.\n")

df = load_loan_data()

while True:
    user_input = input("Your question: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = ai_agent(user_input, df)
    print("\nAI Agent Response:\n")
    print(response)
