import prompt

count = 3


def even_game(get, case):
    print("Welcome to the Brain Games!")
    print(case, end="\n\n")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    for i in range(count):
        question, correct_answer = get()
        print("Question: {}".format(question))
        user_answer = input("Your answer: ")
        if correct_answer == user_answer:
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
