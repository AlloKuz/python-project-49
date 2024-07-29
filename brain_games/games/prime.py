from random import randint

CASE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """Function checks if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_question():
    """function generates a random number between 2 and 100
    and returns it along with whether it is a prime number.
    """
    question = randint(2, 100)
    answer = "yes" if is_prime(question) else "no"
    return question, answer
