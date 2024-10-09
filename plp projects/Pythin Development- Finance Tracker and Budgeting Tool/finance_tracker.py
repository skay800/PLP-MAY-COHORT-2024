import json
import os
import tkinter as tk
from tkinter import messagebox, font, simpledialog
import pandas as pd
import matplotlib.pyplot as plt

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

def add_expense(data, amount, category):
    data["expenses"].append({"amount": amount, "category": category})
    save_data(data)

def delete_transaction(data, transaction_type, index):
    if transaction_type == "income":
        data["income"].pop(index)
    elif transaction_type == "expenses":
        data["expenses"].pop(index)
    save_data(data)

def edit_transaction(data, transaction_type, index, amount, source_or_category):
    if transaction_type == "income":
        data["income"][index] = {"amount": amount, "source": source_or_category}
    elif transaction_type == "expenses":
        data["expenses"][index] = {"amount": amount, "category": source_or_category}
    save_data(data)

def export_data(data):
    df_income = pd.DataFrame(data["income"])
    df_expenses = pd.DataFrame(data["expenses"])
    df_income.to_csv('income.csv', index=False)
    df_expenses.to_csv('expenses.csv', index=False)

def plot_charts(data):
    income = [item["amount"] for item in data["income"]]
    expenses = [item["amount"] for item in data["expenses"]]
    
    labels = ['Total Income', 'Total Expenses']
    sizes = [sum(income), sum(expenses)]
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title("Income vs Expenses")
    plt.show()

class FinanceTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f4f8")  # Light blue background

        # Load data
        self.data = load_data()

        # Create UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_font = font.Font(family="Helvetica", size=16, weight="bold")
        title_label = tk.Label(self.root, text="Finance Tracker", font=title_font, bg="#f0f4f8", fg="#333")
        title_label.pack(pady=20)

        # Income
        self.income_amount = tk.DoubleVar()
        self.income_source = tk.StringVar()
        tk.Label(self.root, text="Income Amount: ", bg="#f0f4f8").pack()
        tk.Entry(self.root, textvariable=self.income_amount).pack()
        tk.Label(self.root, text="Income Source: ", bg="#f0f4f8").pack()
        tk.Entry(self.root, textvariable=self.income_source).pack()
        tk.Button(self.root, text="Add Income", command=self.add_income, bg="#4CAF50", fg="white").pack(pady=5)

        # Expense
        self.expense_amount = tk.DoubleVar()
        self.expense_category = tk.StringVar()
        tk.Label(self.root, text="Expense Amount: ", bg="#f0f4f8").pack()
        tk.Entry(self.root, textvariable=self.expense_amount).pack()
        tk.Label(self.root, text="Expense Category: ", bg="#f0f4f8").pack()
        tk.Entry(self.root, textvariable=self.expense_category).pack()
        tk.Button(self.root, text="Add Expense", command=self.add_expense, bg="#4CAF50", fg="white").pack(pady=5)

        # Budget
        self.budget_amount = tk.DoubleVar()
        tk.Label(self.root, text="Set Budget: ", bg="#f0f4f8").pack()
        tk.Entry(self.root, textvariable=self.budget_amount).pack()
        tk.Button(self.root, text="Set Budget", command=self.set_budget, bg="#4CAF50", fg="white").pack(pady=5)

        # Summary Button
        tk.Button(self.root, text="View Summary", command=self.show_summary, bg="#4CAF50", fg="white").pack(pady=5)
        tk.Button(self.root, text="View All Transactions", command=self.view_all_transactions, bg="#4CAF50", fg="white").pack(pady=5)
        tk.Button(self.root, text="Export Data", command=self.export_data, bg="#4CAF50", fg="white").pack(pady=5)
        tk.Button(self.root, text="Plot Charts", command=self.plot_charts, bg="#4CAF50", fg="white").pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, bg="#FF5733", fg="white").pack(pady=5)

    def add_income(self):
        amount = self.income_amount.get()
        source = self.income_source.get()
        if amount and source:
            add_income(self.data, amount, source)
            self.income_amount.set(0)  # Reset the input field
            self.income_source.set("")   # Reset the input field
        else:
            self.show_error("Please fill in both fields.")

    def add_expense(self):
        amount = self.expense_amount.get()
        category = self.expense_category.get()
        if amount and category:
            add_expense(self.data, amount, category)
            self.expense_amount.set(0)  # Reset the input field
            self.expense_category.set("")  # Reset the input field
        else:
            self.show_error("Please fill in both fields.")

    def set_budget(self):
        budget = self.budget_amount.get()
        if budget:
            set_budget(self.data, budget)
            self.budget_amount.set(0)  # Reset the input field
        else:
            self.show_error("Please enter a budget.")

    def show_summary(self):
        summary = self.view_summary()
        summary_window = tk.Toplevel(self.root)
        summary_window.title("Financial Summary")
        summary_window.geometry("300x200")
        tk.Label(summary_window, text=summary, justify="left").pack(pady=10)

    def view_summary(self):
        total_income = sum(item["amount"] for item in self.data["income"])
        total_expenses = sum(item["amount"] for item in self.data["expenses"])
        remaining_budget = self.data["budget"] - total_expenses if self.data["budget"] else None

        summary = (
            f"Total Income: ${total_income:.2f}\n"
            f"Total Expenses: ${total_expenses:.2f}\n"
        )
        if remaining_budget is not None:
            summary += f"Remaining Budget: ${remaining_budget:.2f}"
        else:
            summary += "Budget not set."
        return summary

    def view_all_transactions(self):
        transaction_window = tk.Toplevel(self.root)
        transaction_window.title("All Transactions")
        transaction_window.geometry("400x400")

        tk.Label(transaction_window, text="Income Transactions", font=("Helvetica", 12)).pack(pady=10)
        for index, income in enumerate(self.data["income"]):
            tk.Label(transaction_window, text=f"{index+1}. ${income['amount']} from {income['source']}").pack()

        tk.Label(transaction_window, text="Expenses Transactions", font=("Helvetica", 12)).pack(pady=10)
        for index, expense in enumerate(self.data["expenses"]):
            tk.Label(transaction_window, text=f"{index+1}. ${expense['amount']} for {expense['category']}").pack()

        tk.Button(transaction_window, text="Close", command=transaction_window.destroy).pack(pady=5)

    def export_data(self):
        export_data(self.data)
        self.show_error("Data exported to income.csv and expenses.csv.")

    def plot_charts(self):
        plot_charts(self.data)

    def show_error(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        error_window.geometry("250x100")
        tk.Label(error_window, text=message, fg="red").pack(pady=20)
        tk.Button(error_window, text="Close", command=error_window.destroy).pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTrackerApp(root)
    root.mainloop()
