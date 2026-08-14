"""
Random Password Generator

Description:
A simple command-line application that generates a random and secure
password based on the length specified by the user.

Concepts Used:
- Variables
- Loops
- Conditional Statements
- User Input
- Exception Handling
- import random
- import string
- String Manipulation
"""
import random
import string

while True:
    print("\n===== RANDOM PASSWORD GENERATOR =====")
    print("1. Generate Password")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":

        try:
            length = int(input("Enter password length: "))

            if length <= 0:
                print("Password length must be greater than 0.")
                continue

            characters = (
                string.ascii_letters +
                string.digits +
                string.punctuation
            )

            password = ""

            for i in range(length):
                password = password + random.choice(characters)

            print("\nGenerated Password:")
            print(password)

        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    elif choice == "2":
        print("Thank you for using the Random Password Generator!")
        break

    else:
        print("Invalid choice! Please enter 1 or 2.")