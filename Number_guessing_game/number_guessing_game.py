# Make user guess a random number
import random

print("Welcome to the Number Guessing Game.\n")
is_playing = input("Wanna begin the game!! ").lower()
if is_playing != "yes":
    quit()

print("\nWhich level you want to play?")
level = input("Easy , Medium or Hard: ").lower()

levels = {"easy": 11 , "medium": 26 , "hard": 51}
if level in levels:
    upper_range = levels[level]
else:
    print("Invalid level. Exiting.")
    quit()

random_number = random.randrange(0, upper_range)
print("\nLet's begin the game: ")

guess_count = 0
user_guess = -1
while user_guess != random_number:
    user_guess = int(input(f"Guess a number between 0 and {upper_range - 1}: "))
    guess_count += 1

print("\nHurray you guessed it correctly.")
print(f"You guessed it in {guess_count} {'try' if guess_count == 1 else 'tries'}.")
