import random

print("Welcome to the Rock Paper Scissor Game!!\n")

def welcome_message():
    response = input("Wanna begin the game!! ").strip().lower()
    return response in ("yes", "y", "sure")


def user_selection():
    print("\nMake your move!")
    while True:
        user_move = input("Rock , Paper or Scissor:- ").strip().lower()
        if user_move not in ["rock", "paper","scissor"]:
            print("Invalid Selection!!")
            continue
        else:
            break
    return user_move


def comp_selection():
    obj_list = ["rock","paper","scissor"]
    comp_choice = random.choice(obj_list)
    print(f"Computer Choice is: {comp_choice}")
    return comp_choice


def play_game(user_move, comp_choice):
    comp_score = 0
    user_score =0
    if user_move == "rock":
        if comp_choice == "paper":
            print("Computer Won!")
            comp_score +=1
        elif comp_choice == "scissor":
            print("You won!")
            user_score += 1
        else:
            print("Draw!")
    elif user_move == "paper":
        if comp_choice == "scissor":
            print("Computer Won!")
            comp_score += 1
        elif comp_choice == "rock":
            print("You won!")
            user_score += 1
        else:
            print("Draw!")
    elif user_move == "scissor":
        if comp_choice == "rock":
            print("Computer Won!")
            comp_score += 1
        elif comp_choice == "paper":
            print("You won!")
            user_score += 1
        else:
            print("Draw!")
    return user_score , comp_score


def score_output(comp_score , user_score):
    print(f"\nComputer Score is: {comp_score}")
    print(f"Your Score is: {user_score}\n")


def main():
    total_user_score = 0
    total_comp_score = 0
    while True:
        if not welcome_message():
            print("Thanks for Playing!!!!")
            quit()

        user_move = user_selection()
        comp_move = comp_selection()

        user_score, comp_score = play_game(user_move, comp_move)

        total_user_score += user_score
        total_comp_score += comp_score

        score_output(total_comp_score, total_user_score)


main()
