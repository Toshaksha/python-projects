import random

print("Welcome to the PIG Dice Roll Game.🐷🎲")
while True:
    try:
        target_score = int(input("Choose a target score (like 20, 50, 100): "))
        break
    except ValueError:
        print("Please enter a valid number!")

user_score = 0

while True:
    response = input("Roll or Hold: ").strip().lower()

    if response not in ("roll", "hold"):
        print("Invalid Command.")
        continue

    if response == "roll":
        num = random.randint(1,6)
        print(f"🎲 Dice Roll: {num}")

        if num == 1:
            user_score = 0
            print(f"Oops! Rolled a 1. No points this turn.")
            print(f"Your Score is: {user_score}")
            break
        else:
            user_score += num
            print("Your Score is:", user_score)
            if user_score >= target_score:
                print("🎉 Congratulations You Won!!!!")
                break
    elif response == "hold":
        print(f"You held at {user_score} points. Game over.")
        break
