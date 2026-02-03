#a number guessing game

#import the require modules
import random
import time

secret_num = random.randint(1, 100)
guesses = 0
max_guesses = 10
low = 1
high = 100
play_again = "yes"

while play_again.lower() == "yes":
    secret_num = random.randint(1, 100)
    guesses = 0
    max_guesses = 10
    low = 1
    high = 100
    start_time = time.time()
    level = int(input("Choose level (1: Easy, 2: Medium, 3: Hard): "))
    if level == 1:
        max_guesses = 15
        range_max = 50
    elif level == 2:
        max_guesses = 10
        range_max = 100
    else:
        max_guesses = 5
        range_max = 200

    secret_num = random.randint(1, range_max)
    hint_count = 3

    while guesses < max_guesses and time.time() - start_time < 60 and hint_count > 0:
        if input("Do you want to play again? (yes/no): ").lower() == "yes":
            hint_count = (low + high) // 2
            print(f"You have {hint_count} hint guesses left, try again.")
            hint_count -= 1
            guesses += 1
        else:
            guess = int(input(f"Guess a number ({low}-{high}): "))
            guesses += 1
            if guess == secret_num:
                score = 1000 - (guesses * 100)
                if score < 0:
                    score = 0
                print(f"Awesome! You got it in {guesses} guesses! Your score is: {score}")
                break
            elif guess < secret_num:
                print("Too low! Try again.")
                low = guess + 1
            else:
                print("Too high! Try again.")
                high = guess - 1
            if guesses == max_guesses:
                print(f"Game over! The number was {secret_num}.")
            if time.time() - start_time > 60:
                print(f"Time's up! The number was {secret_num}.")
                break
    print("=== Welcome to the  number guessing game ===")
    print("Guess the number between 1 and ", range_max)
    print("You have ", max_guesses, "guesses and 60 seconds left")
    print("Type 'hint' for a clue (3 available).")

    import os

    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            high_score = int(file.read())
    else:
        high_score = 0
    if score > high_score:
        with open("highscore.txt", "w") as file:
            file.write(str(score))
        print(f"New high score: {score}!")
    else:
        print(f"High score remains: {high_score}")
    play_again = input("Play again? (yes/no): ").lower()
    try:
        guess = int(input(f"Guess a number ({low}-{high}): "))
    except ValueError:
        print("Please enter a valid number!")
        continue