import random

print("📰 Welcome to the Fake News Headline Generator!")
print("Get ready for some bizarre and hilarious headlines...\n")

list_of_subjects = ["Aliens", "Politicians", "Scientists", "Celebrities"]
list_of_actions = ["declare", "discover", "blame", "ban"]
list_of_objects = ["a new planet", "immortality", "the moon is fake", "talking dogs"]

try:
    while True:
        response = input("Generate a fake news headline? (y/n): ").strip().lower()
        if response == "y":
            print(f"🗞️Headline: {random.choice(list_of_subjects)} {random.choice(list_of_actions)} {random.choice(list_of_objects)}")
        elif response == "n":
            print("Thanks for reading today's fake headlines! 🐶📰")
            break
        else:
            print("⚠️ Invalid Character!! Enter 'y' or 'n'.")
except Exception as e:
    print("Oops ! Something went wrong: ", e)