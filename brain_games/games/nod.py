import prompt
import random
import math
from brain_games.logics import round1, round2, round3


def nod_game1(name):
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    right_answer = math.gcd(number1, number2)
    question = f'{number1} {number2}'
    ans = prompt.string(f'''Find the greatest common divisor of given numbers.
Question: {question} ''')
    return round1(right_answer, ans, name)


def nod_game2(name):
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    right_answer = math.gcd(number1, number2)
    question = f'{number1} {number2}'
    answer = prompt.string(f'Question: {question} ')
    return round2(right_answer, answer, name)


def nod_game3(name):
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    right_answer = math.gcd(number1, number2)
    question = f'{number1} {number2}'
    answer = prompt.string(f'Question: {question} ')
    round3(right_answer, answer, name)


def nod_games(name):
    a = nod_game1(name)
    if a is True:
        return True
    b = nod_game2(name)
    if b is True:
        return True
    nod_game3(name)
