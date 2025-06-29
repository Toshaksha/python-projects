print("Welcome to my Quiz Game!!\n")
playing = input("Do you want to play the Game? ").lower()

if playing != "yes":
    quit()

print("\nOkay, Let's Begin the Adventure!!!! ")
question_list = {
    "Is 2 + 3 = 5?": "Yes",
    "Is the sun a planet?": "No",
    "Is water made of H2O?": "Yes",
    "Is 10 greater than 20?": "No",
    "Is Python a programming language?": "Yes",
    "Does a triangle have 4 sides?": "No",
    "Is the sky usually blue during the day?": "Yes",
    "Is 5 × 5 = 25?": "Yes",
    "Can humans breathe underwater without equipment?": "No",
    "Is ice hot?": "No"
}
total_score = 0
for question in question_list:
    print(f"\nQuestion is:- {question}")
    user_answer = input("Enter your answer( Yes or No): ").strip().lower()
    correct_answer = question_list[question].lower()
    if user_answer == correct_answer:
        total_score += 1
        print("Correct Answer!!!!")
    else:
        print("Oops!!!")
        print(f"Correct answer of this question is: {question_list[question]}")


print(f"\nYour total score out of 10 is {total_score}")
if total_score == 10:
    print("🏆 Excellent! You're a quiz master!")
elif total_score >= 7:
    print("👍 Great job!")
elif total_score >= 5:
    print("🙂 Not bad, keep practicing!")
else:
    print("📘 Better luck next time!")

print(f"Your Pass Percentage is: {(total_score/10) * 100}")