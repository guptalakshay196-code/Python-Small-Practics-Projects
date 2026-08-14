"""
General Knowledge Quiz

Description:
A simple command-line quiz application that asks the user
three general knowledge questions, evaluates the answers,
and displays the final score.

Concepts Used:
- Variables
- User Input
- Conditional Statements (if-else)
- String Manipulation
"""

score = 0

print("===== GENERAL KNOWLEDGE QUIZ =====")
print("Answer the following questions.\n")

#Question 1

answer = input("1. What is the capital of France? ").strip().lower()

if answer == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Paris.\n")

#Question 2

answer = input("2. Which planet is known as the Red Planet? ").strip().lower()

if answer == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Mars.\n")

#Question 3

answer = input("3. How many continents are there on Earth? ").strip()

if answer == "7":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is 7.\n")

#Final Score 

print("===== QUIZ COMPLETED =====")
print(f"Your Final Score: {score}/3")

if score == 3:
    print("Excellent! You got all the answers correct.")

elif score == 2:
    print("Great job! You answered most questions correctly.")

elif score == 1:
    print("Good attempt! Keep learning and try again.")

else:
    print("Don't worry! Practice more and you'll improve.")