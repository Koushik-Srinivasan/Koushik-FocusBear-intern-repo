# Task 5: Number Guessing Game

import random

# Step 1: computer picks a random number between 1 and 10
secret_number = random.randint(1, 10)

# Step 2: keep track of how many guesses the player has made
number_of_guesses = 0

# Step 3: start with a guess that we know is wrong, so the loop begins
current_guess = -1

print("I am thinking of a number between 1 and 10.")

# Step 4: keep asking until the player gets it right
while current_guess != secret_number:
    guess_text = input("Your guess: ")
    current_guess = int(guess_text)
    number_of_guesses = number_of_guesses + 1

    if current_guess < secret_number:
        print("Too low, try again.")
    elif current_guess > secret_number:
        print("Too high, try again.")
    else:
        print("Correct! The number was " + str(secret_number) + ".")
        print("It took you " + str(number_of_guesses) + " attempt(s).")
