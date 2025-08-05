import random

print("Welcome to the PIG Dice Roll Game.")
target_score = 50

user_score = 0

while True:
    response = input("Roll or Hold: ").strip().lower()

    if response not in ("roll", "hold"):
        print("Invalid Command.")
        continue

    if response == "roll":
        num = random.randint(1,6)
        if num == 1:
            print("Dice Roll:", num)
            user_score = 0
            print("Your Score is:", user_score)
            break
        else:
            print("Dice Roll:", num)
            user_score += num
            print("Your Score is:", user_score)
            if user_score >= target_score:
                print("Congratulations You Won!!!!")
                break
    elif response == "hold":
        print("Thanks For Playing!!")
        break
