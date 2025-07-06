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