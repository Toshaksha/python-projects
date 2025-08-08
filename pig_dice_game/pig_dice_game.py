import random

print("Welcome to the PIG Dice Roll Game.🐷🎲")
while True:
    try:
        target_score = int(input("Choose a target score (like 20, 50, 100): "))
        break
    except ValueError:
        print("Please enter a valid number!")

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Players must be between 2 - 4.")
    else:
        print("Invalid , Try Again.")


player_scores = [0 for _ in range(players)]

# game loop
while max(player_scores) < target_score:
    for player_id in range(players):
        print("\nPlayer number ", player_id +1 , "turn has just started.")
        print("Your total score is: ",player_scores[player_id], "\n")
        current_score = 0

        # player turn loop
        while True:
            response = input("Roll or Hold: ").strip().lower()

            if response not in ("roll" , "hold"):
                print("Invalid Command.")
                continue

            if response == "roll":
                num = random.randint(1,6)
                print(f"🎲 Dice Roll: {num}")

                if num == 1:
                    current_score = 0
                    print(f"Oops! Rolled a 1. No points this turn.")
                    print(f"Total score remains: {player_scores[player_id]}")
                    break
                else:
                    current_score +=num
                    print("Your Score is: ", current_score)
            elif response == "hold":
                player_scores[player_id] += current_score
                print(f"You held at {current_score} points. Your total score is now {player_scores[player_id]}")
                break

        if player_scores[player_id] >= target_score:
            print(f"\n🎉 Congratulations Player {player_id + 1}, you won with {player_scores[player_id]} points! 🎉")
            exit()
