from random import randint
from brain_games.engine import even_game

CASE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question():
    question = randint(0, 100)
    answer = "yes" if is_even(question) else "no"
    return question, answer


def run_game():
    even_game(get_question, CASE)
