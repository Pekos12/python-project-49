import prompt
import random
from brain_games.logics import round1, round2, round3


def even_game1(name):
    number1 = random.randint(0, 100)
    if number1 % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = f'{number1}'
    ans = prompt.string(f'Answer "yes" if the number is even, '
                        f'otherwise answer "no".\n'
                        f'Question: {question} ')
    return round1(right_answer, ans, name)


def even_game2(name):
    number2 = random.randint(0, 100)
    if number2 % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = number2
    answer = prompt.string(f'''Question: {question} ''')
    return round2(right_answer, answer, name)


def even_game3(name):
    number3 = random.randint(0, 100)
    if number3 % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = number3
    answer = prompt.string(f'''Question: {question} ''')
    round3(right_answer, answer, name)


def even_games(name):
    a = even_game1(name)
    if a is True:
        return True
    b = even_game2(name)
    if b is True:
        return True
    even_game3(name)
