"""
Expense Tracker

Description:
A simple command-line Expense Tracker built using Python.
This application allows users to enter multiple expenses,
calculates the total amount spent using the accumulator pattern,
and displays the final total.

Concepts Used:
- Variables
- Lists
- Loops (while, for)
- Conditional Statements
- User Input
- append()
- Accumulator Pattern
- Exception Handling
"""
expenses = []

while True:
    print("\n====== EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View Total Spent")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        try:
            expense = float(input("Enter expense amount: ₹"))

            expenses.append(expense)

            print("Expense added successfully!")

        except ValueError:
            print("Invalid amount! Please enter a valid number.")

    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses recorded yet.")

        else:
            total = 0

            for expense in expenses:
                total = total + expense

            print(f"\nTotal Spent: ₹{total:.2f}")

    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")