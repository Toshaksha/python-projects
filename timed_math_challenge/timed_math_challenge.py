import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    expression = str(left) + " " + operator + " " + str(right)
    ans = eval(expression)
    return expression, ans

input("Press enter to start.")
print("------------------------------------")
start_time = time.time()
attempts = 0

for i in range(TOTAL_PROBLEMS):
    expression, ans = generate_problem()
    while True:
        guess = input(f"Problem #{i+1}: {expression} = ")
        try:
            attempts += 1
            if int(guess) == ans:
                break
        except ValueError:
            print("Enter a valid answer.")

end_time = time.time()
total_time = end_time - start_time

print(f"You finished the quiz in {total_time:.2f} seconds with {attempts} attempts.")
