# 2.Number Guessing Game
# Description: Build a game where the computer picks a random number,
# and the player guesses it. The program gives hints (too high/low) until
# the correct guess. This teaches random numbers, loops, and conditionals.
#
# Skills Learned: Random module, loops, conditionals, user input.

import random


def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break


number_guessing_game()

# How to Expand:
# Add a maximum number of attempts.
# Allow the user to choose the range of numbers.
# Keep a high-score list using a file or list.
