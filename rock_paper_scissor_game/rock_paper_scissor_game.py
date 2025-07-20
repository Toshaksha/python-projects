import random

print("🎮 Welcome to the Rock 🪨 Paper 📄 Scissors ✂️ Game!!\n")

# Emoji dictionary for fun output
emoji_map = {
    "rock": "🪨",
    "paper": "📄",
    "scissor": "✂️"
}


def welcome_message():
    response = input("🎲 Wanna begin the game? (yes/no): ").strip().lower()
    return response in ("yes", "y", "sure")


def user_selection():
    print("\nMake your move!")
    while True:
        user_move = input("Choose Rock 🪨, Paper 📄 or Scissor ✂️: ").strip().lower()
        if user_move not in ["rock", "paper", "scissor"]:
            print("❌ Invalid Selection!! Try again.")
            continue
        else:
            break
    return user_move


def comp_selection():
    obj_list = ["rock", "paper", "scissor"]
    comp_choice = random.choice(obj_list)
    print(f"🖥️ Computer chose: {comp_choice.capitalize()} {emoji_map[comp_choice]}")
    return comp_choice


def play_game(user_move, comp_choice):
    comp_score = 0
    user_score = 0

    print(f"\n🧍 You chose: {user_move.capitalize()} {emoji_map[user_move]}")

    if user_move == "rock" and comp_choice == "scissor":
        print("🎉 You won this round!")
        user_score += 1
    elif user_move == "paper" and comp_choice == "rock":
        print("🎉 You won this round!")
        user_score += 1
    elif user_move == "scissor" and comp_choice == "paper":
        print("🎉 You won this round!")
        user_score += 1
    elif user_move == comp_choice:
        print("🤝 It's a Draw!")
    else:
        print("💻 Computer Won this round!")
        comp_score += 1
    return user_score, comp_score


def score_output(comp_score, user_score):
    print(f"\n📊 Scoreboard:")
    print(f"🧍 You: {user_score} | 💻 Computer: {comp_score}")
    print("-" * 30)


def main():
    total_user_score = 0
    total_comp_score = 0

    while True:
        if not welcome_message():
            print("👋 Thanks for Playing! Final Scores:")
            score_output(total_comp_score, total_user_score)
            break

        user_move = user_selection()
        comp_move = comp_selection()
        user_score, comp_score = play_game(user_move, comp_move)

        total_user_score += user_score
        total_comp_score += comp_score

        score_output(total_comp_score, total_user_score)


main()
