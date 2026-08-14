"""
Project: Hangman Game
Author: Lakshay Gupta
Description:
A simple text-based Hangman game where the player
guesses a hidden word one letter at a time.

Concepts Used:
- random module
- while loop
- if-else statements
- strings
- lists
"""

import random
word_list = [
    "python",
    "computer",
    "science",
    "developer",
    "keyboard",
    "hangman",
    "programming",
    "internet",
    "algorithm",
    "database"
]

secret_word = random.choice(word_list)

guessed_letters = []

max_attempts = 6

wrong_attempts = 0

print("=" * 50)
print("🎮 Welcome to the Hangman Game!")
print("=" * 50)
print(f"You have {max_attempts} incorrect guesses.\n")

# Main Game Loop
while wrong_attempts < max_attempts:

    # Create the display word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print(f"You guessed the word: {secret_word}")
        break

    print("Guessed Letters:", guessed_letters)

    print("Remaining Attempts:", max_attempts - wrong_attempts)

    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1:
        print("❌ Please enter only ONE letter.")
        continue

    if not guess.isalpha():
        print("❌ Please enter an alphabet only.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

# Check if the guess is correct
    if guess in secret_word:
        print("✅ Correct Guess!")
    else:
        print("❌ Wrong Guess!")
        wrong_attempts += 1

# Game Over
if wrong_attempts == max_attempts:
    print("\n💀 Game Over!")
    print("You ran out of attempts.")
    print("The correct word was:", secret_word)

print("\nThanks for playing!")