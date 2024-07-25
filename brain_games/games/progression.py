from random import randint
from brain_games.engine import even_game

CASE = "What number is missing in the progression?"

PROGRESSION_LENGHT = 10


def get_progression(start, step, PROGRESSION_LENGHT):
    end = start + (PROGRESSION_LENGHT * step)
    progression = list(range(start, end, step))
    return progression


def get():
    start = randint(1, 100)
    step = randint(1, 10)
    miss_item_index = randint(1, PROGRESSION_LENGHT - 1)
    progression = get_progression(start, step, PROGRESSION_LENGHT)
    answer = progression.pop(miss_item_index)
    progression.insert(miss_item_index, "..")
    question = " ".join([str(i) for i in progression])
    return question, str(answer)


def run_game():
    even_game(get, CASE)
