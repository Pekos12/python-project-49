import prompt
import random


def round1(right_answer, answer, name):
    print(f'Your answer: {answer}')
    if answer == f'{right_answer}':
        print('Correct!')
    else:
        print(f"""'{answer}' is wrong answer ;(.
Correct answer '{right_answer}'.
Let's try again, {name}!""")
        return True


def round2(right_answer, answer, name):
    print(f'Your answer: {answer}')
    if answer == f'{right_answer}':
        print('Correct!')
    else:
        print(f"""'{answer}' is wrong answer ;(.
Correct answer '{right_answer}'.
Let's try again, {name}!""")
        return True


def round3(right_answer, answer, name):
    print(f'Your answer: {answer}')
    if answer == f'{right_answer}':
        print(f'''Correct!
Congratulations, {name}!''')
    else:
        print(f"""'{answer}' is wrong answer ;(.
Correct answer '{right_answer}'.
Let's try again, {name}!""")
        return True
