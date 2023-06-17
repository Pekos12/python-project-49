import prompt
import random
from brain_games.logics import round1, round2, round3


def calc_game1(name):
    tuple_of_deciding = [1, 2, 3]
    decider = random.choice(tuple_of_deciding)
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    if decider == 1:
        question = f'{number1} + {number2}'
        right_answer = number1 + number2
    elif decider == 2:
        question = f'{number1} - {number2}'
        right_answer = number1 - number2
    else:
        question = f'{number1} * {number2}'
        right_answer = number1 * number2
    ans = prompt.string(f'''What is the result of the expression?
Question: {question} ''')
    return round1(right_answer, ans, name)


def calc_game2(name):
    tuple_of_deciding = [1, 2, 3]
    decider = random.choice(tuple_of_deciding)
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    if decider == 1:
        question = f'{number1} + {number2}'
        right_answer = number1 + number2
    elif decider == 2:
        question = f'{number1} - {number2}'
        right_answer = number1 - number2
    else:
        question = f'{number1} * {number2}'
        right_answer = number1 * number2
    answer = prompt.string(f'''Question: {question} ''')
    return round2(right_answer, answer, name)


def calc_game3(name):
    tuple_of_deciding = [1, 2, 3]
    decider = random.choice(tuple_of_deciding)
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    if decider == 1:
        question = f'{number1} + {number2}'
        right_answer = number1 + number2
    elif decider == 2:
        question = f'{number1} - {number2}'
        right_answer = number1 - number2
    else:
        question = f'{number1} * {number2}'
        right_answer = number1 * number2
    answer = prompt.string(f'''Question: {question} ''')
    return round3(right_answer, answer, name)


def calc_games(name):
    a = calc_game1(name)
    if a is True:
        return True
    b = calc_game2(name)
    if b is True:
        return True
    calc_game3(name)
