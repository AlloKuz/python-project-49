from random import randint

CASE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Function checks whether the passed number is even"""
    return number % 2 == 0


def get_question():
    """Function generates a random number between 0 and 100
    and returns it along with whether it is an even number.
    """
    question = randint(0, 100)
    answer = "yes" if is_even(question) else "no"
    return question, answer
