from random import randint
from brain_games.engine import even_game

CASE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_question():
    question = randint(2, 100)
    answer = "yes" if is_prime(question) else "no"
    return question, answer


def run_game():
    even_game(get_question, CASE)
