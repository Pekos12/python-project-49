import prompt
import random


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def calc_game1():
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
    answer = prompt.string(f'''What is the result of the expression?
Question: {question} ''')
    print(f'Your answer: {answer}')
    if answer == f'{right_answer}':
        print('Correct!')
    else:
        print(f"""'{answer}' is wrong answer ;(.
Correct answer '{right_answer}'.
Let's try again, {name}!""")
        return True


def calc_game2():
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
    print(f'Your answer: {answer}')
    if answer == f'{right_answer}':
        print('Correct!')
    else:
        print(f"""'{answer}' is wrong answer ;(.
Correct answer '{right_answer}'.
Let's try again, {name}!""")
        return True


def calc_game3():
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
    print(f'Your answer: {answer}')
    if answer == f'{right_answer}':
        print(f'''Correct!
Congratulations, {name}!''')
    else:
        print(f"""'{answer}' is wrong answer ;(.
Correct answer '{right_answer}'.
Let's try again, {name}!""")
        return True


def calc_games():
    a = calc_game1()
    if a is True:
        return True
    b = calc_game2()
    if b is True:
        return True
    calc_game3()
