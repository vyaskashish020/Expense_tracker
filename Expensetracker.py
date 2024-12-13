import csv
from datetime import datetime

expenses = []
monthly_budget = 0.0

# Add an Expense
def add_expense():
    print("\nAdd an Expense")
    try:
        date = input("Enter the date (YYYY-MM-DD): ")
        datetime.strptime(date, "%Y-%m-%d")  

        category = input("Enter the category (e.g., Food, Travel): ")
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a short description: ")

        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }
        expenses.append(expense)
        print("Expense recorded successfully!\n")
    except ValueError as error:
        print(f"Invalid input: {error}. Please try again.\n")

# View Expenses
def view_expenses():
    print("\n--- View Expenses ---")
    if not expenses:
        print("No expenses have been recorded yet.\n")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. Date: {expense['date']}, Category: {expense['category']}, "
              f"Amount: {expense['amount']}, Description: {expense['description']}")
    print()

# Set and Track Monthly Budget
def set_budget():
    global monthly_budget
    try:
        monthly_budget = float(input("\nEnter your monthly budget: "))
        print(f"Your monthly budget is set to {monthly_budget:.2f}.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

def track_budget():
    if monthly_budget == 0:
        print("\nYou have not set a monthly budget. Please set it first.\n")
        return

    total_spent = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: {total_spent:.2f}")
    if total_spent > monthly_budget:
        print("Alert: You have exceeded your budget!\n")
    else:
        remaining_budget = monthly_budget - total_spent
        print(f"You have {remaining_budget:.2f} remaining for this month.\n")

# Save and Load Expenses
def save_expenses():
    try:
        with open("expenses.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
            writer.writeheader()
            writer.writerows(expenses)
        print("Expenses saved successfully to 'expenses.csv'.\n")
    except Exception as error:
        print(f"An error occurred while saving expenses: {error}\n")

def load_expenses():
    global expenses
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            expenses = [
                {
                    'date': row['date'],
                    'category': row['category'],
                    'amount': float(row['amount']),
                    'description': row['description']
                }
                for row in reader
            ]
        print("Expenses loaded from the file successfully!\n")
    except FileNotFoundError:
        print("No saved expenses were found. Starting fresh.\n")
    except Exception as error:
        print(f"An error occurred while loading expenses: {error}\n")

# Display Interactive Menu
def display_menu():
    print("\n--- Personal Expense Tracker ---")
    print("1. Add a New Expense")
    print("2. View All Expenses")
    print("3. Set Your Monthly Budget")
    print("4. Track Budget Usage")
    print("5. Save Expenses to File")
    print("6. Exit Program")

def main():
    load_expenses()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            set_budget()
        elif choice == '4':
            track_budget()
        elif choice == '5':
            save_expenses()
        elif choice == '6':
            save_expenses()
            print("Thank you for using our application")
            break
        else:
            print("Invalid option. Please select a valid menu choice.\n")

if __name__ == "__main__":
    main()