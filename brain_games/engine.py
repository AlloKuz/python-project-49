import prompt

COUNT = 3


def even_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.CASE, end="\n\n")
    for i in range(COUNT):
        question, correct_answer = game.get_question()
        print("Question: {}".format(question))
        user_answer = prompt.string('Your answer: ')
        if str(correct_answer) == user_answer:
            print("Correct!")
        else:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                    user_answer, correct_answer
                )
            )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
