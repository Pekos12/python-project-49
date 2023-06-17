import prompt
import random
from brain_games.logics import round1, round2, round3


def progression_game1(name):
    len_of_list = random.randint(5, 13)
    i = 0
    list = [random.randint(0, 100)]
    n = random.randint(0, 100)
    while i < len_of_list - 1:
        b = list[-1] + n
        list.append(b)
        i += 1
    chosen_number = random.randint(0, len(list) - 1)
    right_answer = list[chosen_number]
    list[chosen_number] = '..'
    final = ' '.join(map(str, list))
    question = f'{final}'
    answer = prompt.string(f'''What number is missing in the progression?
Question: {question} ''')
    return round1(right_answer, answer, name)


def progression_game2(name):
    len_of_list = random.randint(5, 13)
    i = 0
    list = [random.randint(0, 100)]
    n = random.randint(0, 100)
    while i < len_of_list - 1:
        b = list[-1] + n
        list.append(b)
        i += 1
    chosen_number = random.randint(0, len(list) - 1)
    right_answer = list[chosen_number]
    list[chosen_number] = '..'
    final = ' '.join(map(str, list))
    question = f'{final}'
    answer = prompt.string(f'Question: {question} ')
    return round2(right_answer, answer, name)


def progression_game3(name):
    len_of_list = random.randint(5, 13)
    i = 0
    list = [random.randint(0, 100)]
    n = random.randint(0, 100)
    while i < len_of_list - 1:
        b = list[-1] + n
        list.append(b)
        i += 1
    chosen_number = random.randint(0, len(list) - 1)
    right_answer = list[chosen_number]
    list[chosen_number] = '..'
    final = ' '.join(map(str, list))
    question = f'{final}'
    answer = prompt.string(f'Question: {question} ')
    round3(right_answer, answer, name)


def progression_games(name):
    a = progression_game1(name)
    if a is True:
        return True
    b = progression_game2(name)
    if b is True:
        return True
    progression_game3(name)
