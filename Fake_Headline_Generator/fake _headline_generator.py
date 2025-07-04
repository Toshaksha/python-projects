import random

print("📰 Welcome to the Fake News Headline Generator!")
print("Get ready for some bizarre and hilarious headlines...")

def space_headlines():
    space_subjects = ["Aliens", "NASA", "Astronauts", "Martians", "Black holes", "Moon colonies"]
    space_actions = ["discover", "colonize", "warn about", "teleport to", "ban", "make peace with"]
    space_objects = ["a new galaxy", "talking asteroids", "a moon made of cheese", "the edge of the universe",
                     "Martian disco clubs", "space whales"]
    headline = random.choice(space_subjects) + " " + random.choice(space_actions) + " " + random.choice(space_objects)
    return headline

def politics_headlines():
    politics_subjects = ["Politicians", "Presidents", "Government officials", "Senators", "World leaders", "Mayors"]
    politics_actions = ["blame", "ban", "announce", "leak", "legalize", "investigate"]
    politics_objects = ["gravity", "public dancing", "cloning technology", "reverse taxes", "time travel passports", "robot advisors"]
    headline = random.choice(politics_subjects) + " " + random.choice(politics_actions) + " " + random.choice(politics_objects)
    return headline

def sports_headlines():
    sports_subjects = ["Football players", "Olympians", "Coaches", "Referees", "Cricket teams", "Fans"]
    sports_actions = ["challenge", "defeat", "train with", "replace", "ban", "hire"]
    sports_objects = ["invisible balls", "AI umpires", "telepathic teammates", "alien cheerleaders", "hoverboots",
                      "3D printed stadiums"]
    headline = random.choice(sports_subjects) + " " + random.choice(sports_actions) + " " + random.choice(sports_objects)
    return headline

def tech_headlines():
    tech_subjects = ["AI", "Robots", "Tech CEOs", "Hackers", "Startups", "Quantum computers"]
    tech_actions = ["invent", "hack", "replace", "predict", "leak", "upload consciousness to"]
    tech_objects = ["digital brains", "flying laptops", "sentient memes", "auto-coding cats", "quantum TikTok",
                    "cyber noodles"]
    headline = random.choice(tech_subjects) + " " + random.choice(tech_actions) + " " + random.choice(tech_objects)
    return headline

def myths_headlines():
    myth_subjects = ["Ghosts", "Bigfoot", "Vampires", "Witches", "Time travelers", "Psychics"]
    myth_actions = ["summon", "haunt", "reveal", "communicate with", "accidentally curse", "teleport to"]
    myth_objects = ["the underworld", "ancient prophecies", "a haunted subway", "mystic pizza", "eternal Mondays",
                    "cursed social media posts"]
    headline = random.choice(myth_subjects) + " " + random.choice(myth_actions) + " " + random.choice(myth_objects)
    return headline

genre_functions = {
    "space": space_headlines,
    "politics": politics_headlines,
    "sports": sports_headlines,
    "tech&ai": tech_headlines,
    "myths&paranormal": myths_headlines
}

try:
    while True:
        response = input("\nGenerate a fake news headline? (y/n): ").strip().lower()
        if response == "y":
            print("Here is the list of Genres: ")
            for keys in genre_functions:
                print(f"{keys.title()}")
            choice = input("Enter your choice of genre: ").strip().lower()
            if choice in genre_functions:
                print(f"🗞️Headline: {genre_functions[choice]()}")
            else:
                print("⚠️ Invalid genre! Please choose from the listed options.")
        elif response == "n":
            print("🚀 Thanks for reading today's fake headlines!")
            print("Remember: if you see 'talking dogs' on the street... we warned you. 🐶📰")
            break
        else:
            print("⚠️ Invalid Character!! Enter 'y' or 'n'.")
except Exception as e:
    print("Oops ! Something went wrong: ",e)