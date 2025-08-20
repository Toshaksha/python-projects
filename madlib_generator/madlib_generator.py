import random

def story_1():
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb ending with -ing: ")
    emotion = input("Enter an emotion: ")
    past_verb = input("Enter a past tense verb: ")
    print(f"One day, I went to the {place} and saw a {adjective} {animal} {verb} at me. I was so {emotion}, I {past_verb}!")

def story_2():
    food = input("Enter a type of food: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb ending with -ing: ")
    family_member = input("Enter a family member: ")
    emotion = input("Enter an emotion: ")
    print(f"Yesterday, I tried to make {food}, added too much {noun}, and it started {verb}. My {family_member} was so {emotion}!")

stories = [story_1, story_2]
random.choice(stories)()