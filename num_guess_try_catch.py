#!/usr/bin/env python3
# Created by: Anastasia Friedenstein Patino
# Created on: October. 26, 2023
# Guessing game of numbers 1 to 9 with try catch
import random


def main():
    # Generate a random number between 1 and 9
    random_number = random.randint(1, 9)

    # Get the user's guess as an integer

    guess_as_string = input("Enter your guess:")

    try:
        guess_as_int = int(guess_as_string)
        # Check if the guess is correct
        if guess_as_int == random_number:
            print("You guessed correctly!")
        else:
            print(f"You guessed wrong. The correct answer was: {random_number}")
    except:
        print(f" {guess_as_string} is not a valid integer.")
    finally:
        print("Thank you for playing")


if __name__ == "__main__":
    main()
