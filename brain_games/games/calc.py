from random import choice, choices

CASE = "What is the result of the expression?"

SIGN = ["+", "-", "*"]


def calculate(num_1, num_2, sign):
    if sign == "+":
        result = num_1 + num_2
    elif sign == "-":
        result = num_1 - num_2
    elif sign == "*":
        result = num_1 * num_2
    return result


def get_question():
    num1, num2 = choices(range(1, 30), k=2)
    sign = choice(SIGN)
    answer = calculate(num1, num2, sign)
    question = "{} {} {}".format(num1, sign, num2)
    return question, answer
