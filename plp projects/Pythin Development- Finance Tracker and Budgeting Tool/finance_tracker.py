# finance_tracker/finance_tracker.py

import json
import os

DATA_FILE = 'data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {"income": [], "expenses": [], "budget": 0}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_income(data, amount, source):
    data["income"].append({"amount": amount, "source": source})
    save_data(data)
    print(f"Added income: ${amount} from {source}")

def add_expense(data, amount, category):
    data["expenses"].append({"amount": amount, "category": category})
    save_data(data)
    print(f"Added expense: ${amount} for {category}")

def set_budget(data, budget):
    data["budget"] = budget
    save_data(data)
    print(f"Budget set to: ${budget}")

def view_summary(data):
    total_income = sum(item["amount"] for item in data["income"])
    total_expenses = sum(item["amount"] for item in data["expenses"])
    remaining_budget = data["budget"] - total_expenses if data["budget"] else None

    print("\n--- Financial Summary ---")
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    if remaining_budget is not None:
        print(f"Remaining Budget: ${remaining_budget}")
    else:
        print("Budget not set.")

def main():
    data = load_data()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Set Budget")
        print("4. View Summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            source = input("Enter income source: ")
            add_income(data, amount, source)

        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            add_expense(data, amount, category)

        elif choice == '3':
            budget = float(input("Enter your budget: "))
            set_budget(data, budget)

        elif choice == '4':
            view_summary(data)

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
