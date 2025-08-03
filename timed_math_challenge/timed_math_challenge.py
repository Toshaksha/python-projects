import random

OPERATORS = ["+", "-", "*", "/"]
MIN_OPERAND = 2
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    expression = str(left) + " " + operator + " " + str(right)
    ans = eval(expression)
    print(ans)


generate_problem()