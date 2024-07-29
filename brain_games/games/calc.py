from random import choice, choices

CASE = "What is the result of the expression?"

SIGNS = ["+", "-", "*"]


def calculate(num_1, num_2, sign):
    """Function performs arithmetic operations of addition,
    subtraction and multiplication on two numbers.
    """
    if sign == "+":
        result = num_1 + num_2
    elif sign == "-":
        result = num_1 - num_2
    elif sign == "*":
        result = num_1 * num_2
    return result


def get_question():
    """Function generates a math question with two numbers and an operator."""
    num1, num2 = choices(range(1, 30), k=2)
    sign = choice(SIGNS)
    answer = calculate(num1, num2, sign)
    question = "{} {} {}".format(num1, sign, num2)
    return question, answer
