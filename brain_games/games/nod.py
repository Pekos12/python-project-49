import prompt
import random
import math
from brain_games.logics import round1, round2, round3


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def nod_game1():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    right_answer = math.gcd(number1, number2)
    question = f'{number1} {number2}'
    ans = prompt.string(f'''Find the greatest common divisor of given numbers.
Question: {question} ''')
    return round1(right_answer, ans, name)


def nod_game2():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    right_answer = math.gcd(number1, number2)
    question = f'{number1} {number2}'
    answer = prompt.string(f'Question: {question} ')
    return round2(right_answer, answer, name)


def nod_game3():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    right_answer = math.gcd(number1, number2)
    question = f'{number1} {number2}'
    answer = prompt.string(f'Question: {question} ')
    round3(right_answer, answer, name)


def nod_games():
    a = nod_game1()
    if a is True:
        return True
    b = nod_game2()
    if b is True:
        return True
    nod_game3()
