import prompt
import random
from brain_games.logics import round1, round2, round3


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def prime_game1():
    number1 = random.randint(0, 1000)
    if number1 == 2:
        right_answer = 'yes'
    if number1 < 2:
        right_answer = 'no'
    k = 0
    for i in range(2, number1 // 2 + 1):
        if (number1 % i == 0):
            k += 1
    if k == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = f'{number1}'
    ans = prompt.string(f'Answer "yes" if given number is prime. '
                        f'Otherwise answer "no".\n'
                        f'Question: {question} ')
    return round1(right_answer, ans, name)


def prime_game2():
    number1 = random.randint(0, 1000)
    if number1 == 2:
        right_answer = 'yes'
    if number1 < 2:
        right_answer = 'no'
    k = 0
    for i in range(2, number1 // 2 + 1):
        if (number1 % i == 0):
            k += 1
    if k == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = f'{number1}'
    answer = prompt.string(f'Question: {question} ')
    return round2(right_answer, answer, name)


def prime_game3():
    number1 = random.randint(0, 1000)
    if number1 == 2:
        right_answer = 'yes'
    if number1 < 2:
        right_answer = 'no'
    k = 0
    for i in range(2, number1 // 2 + 1):
        if (number1 % i == 0):
            k += 1
    if k == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = f'{number1}'
    answer = prompt.string(f'Question: {question} ')
    round3(right_answer, answer, name)


def prime_games():
    a = prime_game1()
    if a is True:
        return True
    b = prime_game2()
    if b is True:
        return True
    prime_game3()
