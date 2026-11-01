def add_expense(expenses, category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
    return expenses

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        print("Expenses by category:")
        for category, amount in expenses.items():
            print(f"{category}: ₹{amount}")

def total_expenses(expenses):
    return sum(expenses.values())

def main():
    expenses = {}
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            category = input("Enter expense category: ")
            try:
                amount = float(input("Enter expense amount: ₹ "))
                if amount < 0:
                    print("Amount cannot be negative.")
                else:
                    expenses = add_expense(expenses, category, amount)
                    print(f"Added expense: {category} - ₹{amount}")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            total = total_expenses(expenses)
            print(f"Total expenses: ₹{total}")
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()