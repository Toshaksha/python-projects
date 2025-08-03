import random

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

for i in range(TOTAL_PROBLEMS):
    expression, ans = generate_problem()
    while True:
        guess = input(f"Problem #{i+1}: {expression} = ")
        if guess == str(ans):
            break
