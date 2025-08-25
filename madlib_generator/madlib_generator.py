import random

print("🎲 Welcome to the Random Mad Lib Generator!")
print("Ready to experience the madness!!")


def story_1():
    print(f"\nOne day, I decided to go to the [place]. Suddenly, I saw a [adjective] [animal] [a verb ending with -ing] towards me. I was so [emotion] that I [a past tense verb] away!")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb ending with -ing: ")
    emotion = input("Enter an emotion: ")
    past_verb = input("Enter a past tense verb: ")
    print("\n🎉 Here's your story:\n")
    print(f"One day, I decided to go to the {place}. Suddenly, I saw a {adjective} {animal} {verb} towards me. I was so {emotion} that I {past_verb} away!")


def story_2():
    print(f"\nYesterday, I tried to make a [food]. I added too much [noun], and it started [a verb ending with -ing] all over the kitchen. My [family_member] was so [emotion]!")
    food = input('Enter a type of food: ')
    noun = input('Enter a noun: ')
    verb = input('Enter a verb ending with -ing: ')
    family_member = input('Enter a family member: ')
    emotion = input('Enter an emotion: ')
    print("\n🎉 Here's your story:\n")
    print(f"Yesterday, I tried to make a {food}. I added too much {noun}, and it started {verb} all over the kitchen. My {family_member} was so {emotion}!")


def story_3():
    print(f"\nToday at the zoo, I saw a [adjective] [animal] eating [food]. It was [a verb ending with -ing] and making [noise] sounds.")
    adjective = input('Enter an adjective: ')
    animal = input('Enter an animal: ')
    food = input('Enter a type of food: ')
    verb = input('Enter a verb ending with -ing: ')
    noise = input('Enter a noise: ')
    print("\n🎉 Here's your story:\n")
    print(f"Today at the zoo, I saw a {adjective} {animal} eating {food}. It was {verb} and making {noise} sounds.")


def story_4():
    print(f"\nMy last vacation was to [place]. I went with my [relation], and we spent the days [verb] on the beach. The weather was so [adjective] and the food was [adjective2]!")
    place = input('Enter a place: ')
    relation = input('Enter a relation: ')
    verb = input('Enter a verb ending with -ing: ')
    adjective = input('Enter an adjective: ')
    adjective2 = input('Enter an adjective: ')
    print("\n🎉 Here's your story:\n")
    print(f"My last vacation was to {place}. I went with my {relation}, and we spent the days {verb} on the beach. The weather was so {adjective} and the food was {adjective2}!")


def story_5():
    print("\nIn a [adjective] forest, a [creature] was [verb ending in -ing] while holding a [object]. It vanished into thin air!")
    adjective = input("Enter an adjective: ")
    creature = input("Enter a mythical creature: ")
    verb = input("Enter a verb ending with -ing: ")
    objects = input("Enter a magical object: ")
    print("\n🎉 Here's your story:\n")
    print(f"In a {adjective} forest, a {creature} was {verb} while holding a {objects}. It vanished into thin air!")

def story_6():
    print("\nOnce, I dreamt I was a [profession] in [place], carrying a [objects] and [verb] down the street like a hero!")
    profession = input("Enter a profession: ")
    place = input("Enter a place: ")
    objects = input("Enter an object: ")
    verb = input("Enter a verb ending in -ing: ")
    print("\n🎉 Here's your story:\n")
    print(f"Once, I dreamt I was a {profession} in {place}, carrying a {objects} and {verb} down the street like a hero!")

def story_7():
    print("\nAt school, my teacher turned into a [color] [animal], and everyone was [emotion] until she started to [verb]!")
    animal = input("Enter an animal: ")
    color = input("Enter a color: ")
    emotion = input("Enter an emotion: ")
    verb = input("Enter a verb: ")
    print("\n🎉 Here's your story:\n")
    print(f"At school, my teacher turned into a {color} {animal}, and everyone was {emotion} until she started to {verb}!")

def story_8():
    print("\nIn the future, cars will be powered by [noun], [verb] down the street while going [sound]!")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb ending with -ing: ")
    sound = input("Enter a sound: ")
    print("\n🎉 Here's your story:\n")
    print(f"In the future, cars will be powered by {noun}, {verb} down the street while going {sound}!")

def story_9():
    print("\nMy pet [animal] just learned to [verb] and now wants to play [game] every day!")
    animal = input("Enter a pet: ")
    verb = input("Enter a verb: ")
    game = input("Enter a game: ")
    print("\n🎉 Here's your story:\n")
    print(f"My pet {animal} just learned to {verb} and now wants to play {game} every day!")

def story_10():
    print("\nBreaking news! A [adjective] alien named [alien_name] was found in [place], [verb] near a taco stand!")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
    alien_name = input("Enter a name: ")
    verb = input("Enter a verb ending with -ing: ")
    print("\n🎉 Here's your story:\n")
    print(f"Breaking news! A {adjective} alien named {alien_name} was found in {place}, {verb} near a taco stand!")


stories = [
    story_1, story_2, story_3, story_4, story_5,
    story_6, story_7, story_8, story_9, story_10
]

while True:
    random.choice(stories)()

    while True:  # input validation loop
        again = input("\n🎉 Want to play again? (y/n): ").strip().lower()
        if again == 'y':
            break  # break inner loop, continue outer loop
        elif again == 'n':
            print("Thanks for playing! 🥳")
            exit()  # exit the program entirely
        else:
            print("❌ Invalid input! Please enter 'y' or 'n'.")
