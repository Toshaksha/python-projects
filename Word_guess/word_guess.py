import random

print("Welcome aboard.\nReady to solve the mysteries!!")
print("""Rules:
- You will be given a word to guess based on the difficulty you choose.
- You will be told how many letters are there in the word.
- After every guess, you'll be told whether you made a correct guess or not.
- Keep guessing until you guess the word correctly.
- Type 'q' at any time to quit the game.""")

easy_words = [
    "cat", "dog", "sun", "book", "tree","fish", "car", "milk", "bird", "cake"
]

medium_words = [
    "planet", "guitar", "window", "garden", "puzzle","banana", "bottle", "button", "castle", "pencil"
]

hard_words = [
    "microscope", "astronaut", "dinosaur", "triangle", "elephant","volcano", "telescope", "backpack", "algorithm", "kangaroo"
]

def levels():
    while True:
        print("What level you wanna play: Easy, Medium or Hard")
        user_level = input("> ").strip().lower()
        if user_level == "easy":
            word = random.choice(easy_words)
            return word
        elif user_level == "medium":
            word = random.choice(medium_words)
            return word
        elif user_level == "hard":
            word = random.choice(hard_words)
            return word
        else:
            print("Invalid level.")

def no_of_letters(word):
    print("Number of letters in the word is: ", len(word))

def game_logic():
    no_of_guesses = 0
    word = levels()
    no_of_letters(word)
    user_guess = "_" * len(word)
    guess_list = list(user_guess)

    while True:
        print("Current guess:", "".join(guess_list))
        character = input("Enter a letter (or 'q' to quit): ").strip().lower()

        if character == 'q':
            print("Game quit. The word was:", word)
            break

        no_of_guesses += 1
        if character in word:
            for index, item in enumerate(word):
                if item == character:
                    guess_list[index] = character
        else:
            print("Wrong guess!")

        user_guess = "".join(guess_list)

        if user_guess == word:
            print("Congratulations!!! You guessed the word correctly in", no_of_guesses, "guesses.")
            break