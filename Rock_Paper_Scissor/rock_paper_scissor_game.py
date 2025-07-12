import random

print("Welcome to the Rock Paper Scissor Game!!\n")
print("Make your move!")
user_move = input("Rock , Paper or Scissor:- ").strip().lower()

if user_move not in ["rock", "paper", "scissor"]:
    print("Please enter correct option.")
    quit()

obj_list = ["rock", "paper", "scissor"]
comp_move = random.choice(obj_list)
print(f"Computer choose: {comp_move}")

if user_move == "rock":
    if comp_move == "paper":
        print("Computer Won!")
    elif comp_move == "scissor":
        print("You won!")
    else:
        print("Draw!")
elif user_move == "paper":
    if comp_move == "scissor":
        print("Computer Won!")
    elif comp_move == "rock":
        print("You won!")
    else:
        print("Draw!")
elif user_move == "scissor":
    if comp_move == "rock":
        print("Computer Won!")
    elif comp_move == "paper":
        print("You won!")
    else:
        print("Draw!")
