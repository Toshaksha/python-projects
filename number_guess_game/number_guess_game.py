import random

def welcome_screen():
    print("🎮 Welcome to the Number Guessing Game.\n")
    response = input("🎲 Ready to test your luck? Let's begin! (yes/no): ").strip().lower()
    return response in ("yes", "y","sure")


def select_level():
    levels = {"easy": 11, "medium": 26, "hard": 51}
    while True:
        level = input("Choose your level (Easy , Medium or Hard): ").strip().lower()
        if level in levels:
            return levels[level]
        else:
            print("❌ Invalid level. Please Try Again.\n")


def play_game(upper_range):
    random_number = random.randint(0, upper_range - 1)
    print(f"\n🔢 Number Range is between 0 and {upper_range-1}. Start guessing!\n")

    guess_count = 0
    while True :
        try:
            guess = int(input("Your Guess: "))
            guess_count +=1

            if guess < random_number:
                print("📉 Too low!")
            elif guess > random_number:
                print("📈 Too high!")
            else:
                print(f"\n🎉 Hurray! You guessed it in {guess_count} {'try' if guess_count == 1 else 'tries'}.\n")
                break
        except ValueError:
            print("⚠️ Please enter a valid integer.")


def ask_reply():
    answer = input("Do you want to play again? (yes/no): ").strip().lower()
    return answer in ("yes" , "y" , "sure")


def game():
    while True:
        if not welcome_screen():
            print("👋 Goodbye!!")
            break

        upper_range = select_level()
        play_game(upper_range)

        if not ask_reply():
            print("🙌 Thank you for playing!! See you next time.\n")
            break

# start the game
game()