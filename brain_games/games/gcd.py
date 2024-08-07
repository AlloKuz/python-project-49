from random import choices

CASE = "Find the greatest common divisor of given numbers."


def get_gcd(num1, num2):
    """Function finds the greatest common divisor (GCD)
    of two positive integers.
    """
    min_num, max_num = min(num1, num2), max(num1, num2)
    divisor = min_num
    while divisor > 0:
        if max_num % divisor == 0 and min_num % divisor == 0:
            return divisor
        divisor -= 1


def get_question():
    """The function generates a pair of random numbers
    and returns them along with their greatest common divisor.
    """
    num1, num2 = choices(range(1, 30), k=2)
    question = "{} {}".format(num1, num2)
    answer = get_gcd(num1, num2)
    return question, answer
