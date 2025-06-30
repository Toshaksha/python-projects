import random

list_of_subjects = ["Aliens", "Politicians", "Scientists", "Celebrities"]
list_of_actions = ["declare", "discover", "blame", "ban"]
list_of_objects = ["a new planet", "immortality", "the moon is fake", "talking dogs"]

while True:
    response = input("Want to generate a news headline (y/n): ").strip().lower()
    if response == "y":
        print(f"{random.choice(list_of_subjects)} {random.choice(list_of_actions)} {random.choice(list_of_objects)}")
    elif response == "n":
        break
    else:
        print("Invalid Character!! Enter 'y' or 'n'.")