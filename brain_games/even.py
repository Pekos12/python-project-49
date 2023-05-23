import prompt
import random


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def even_game1():
    number1 = random.randint(0, 100)
    if number1 % 2 == 0:
        right_answer1 = 'yes'
    else:
        right_answer1 = 'no'
    answer1 = prompt.string(f'''Answer "yes" if the number is even,
otherwise answer "no".
Question: {number1} ''')
    print(f'Your answer: {answer1}')
    if answer1 == right_answer1:
        print('Correct!')
    else:
        print(f"""'{answer1}' is wrong answer ;(.
Correct answer '{right_answer1}'.
Let's try again, {name}!""")
        return True


def even_game2():
    number2 = random.randint(0, 100)
    if number2 % 2 == 0:
        right_answer2 = 'yes'
    else:
        right_answer2 = 'no'
    answer2 = prompt.string(f'''Question: {number2} ''')
    print(f'Your answer: {answer2}')
    if answer2 == right_answer2:
        print('Correct!')
    else:
        print(f"""'{answer2}' is wrong answer ;(.
Correct answer '{right_answer2}'.
Let's try again, {name}!""")
        return True


def even_game3():
    number3 = random.randint(0, 100)
    if number3 % 2 == 0:
        right_answer3 = 'yes'
    else:
        right_answer3 = 'no'
    answer3 = prompt.string(f'''Question: {number3} ''')
    print(f'Your answer: {answer3}')
    if answer3 == right_answer3:
        print(f'''Correct!
Congratulations, {name}!''')
    else:
        print(f"""'{answer3}' is wrong answer ;(.
Correct answer '{right_answer3}'.
Let's try again, {name}!""")


def even_games():
    a = even_game1()
    if a is True:
        return True
    b = even_game2()
    if b is True:
        return True
    even_game3()
