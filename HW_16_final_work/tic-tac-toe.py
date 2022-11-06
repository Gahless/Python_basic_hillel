import time
import json
import random

with open('data.txt', 'r') as f:
    data = json.load(f)

player1 = 'player1'
player2 = 'player2'
if data['settings']['число игроков'][0] == '1':
    player2 = 'computer'

def roll():
    return random.choice([True, False])


def _input():
    global user_input
    user_input = input('>>>')
    user_input = user_input.lower()


def menu():
    print('''Добро пожаловать в игру "Крестики-нолики"''')
    print('''Для просмотра правил введите "rules"
Для изменения настроек введите "settings"
Для просмотра всех доступных команд введите "help"
\nДля начала игры введите "start"''')


def rules():
    print('''Правила игры:
Размер поля - 3 на 3 клетки. гроки по очереди ставят свой символ (крестик или нолик) на незанятю клетку поля,
крестики всегда ходят первыми. Побеждает первый игрок собравший ряд из трех свох символов (по горизонтали,
вертикалиили или диогонали)\n''')

    time.sleep(2)
    menu()


def help():
    print('''Список всех команд:
help - показать все команды
menu - вернуться в начальное меню
rules - правила игры
settings - настройка игры
start - начать игру
restart - перезапустить игру
score - показать счет с компьютером
delete_score - сбросить счет с компьютером
rename - поменять имя
exit - закрыть программу
''')


def settings_change():
    global player1, player2
    _input()

    if user_input in commands:
        pass
    elif user_input not in data['settings']:
        print('Команда не распознана. Чтобы изменить настройку введите ее название. "help" для посмотра всех команд')
    else:
        print(f'доступные значения для {user_input}: {data["settings"][user_input][1]}, на что меняем?')
        setting = user_input
        _input()

        if user_input in data["settings"][setting][2]:
            data["settings"][setting][0] = user_input
            with open('data.txt', 'w') as f:
                json.dump(data, f)
        else:
            print(f'{user_input} неподходящее значение для {setting}')

    player1 = 'player1'
    player2 = 'player2'
    if data['settings']['число игроков'][0] == '1':
        player2 = 'computer'


def settings():
    global data, user_input

    user_input = '---'

    while user_input not in commands:
        for key in data['settings']:
            print(f'{key}: {data["settings"][key][0]}')
        print('\nЖелаете что-то изменить? ("help" для посмотра всех команд)')

        settings_change()
    exec(f'{user_input}()')


def score():
    global data
    for difficulties in data['score']:
        print(f'{difficulties}: | ', end='')
        for key in data['score'][difficulties]:
            print(f'{key}: {data["score"][difficulties][key]}', end=' | ')
        print()


def delete_score():
    data['score'] = {
        'сложность 1': {'Побед': 0, 'Поражений': 0, 'Ничьих': 0},
        'сложность 2': {'Побед': 0, 'Поражений': 0, 'Ничьих': 0},
        'сложность 3': {'Побед': 0, 'Поражений': 0, 'Ничьих': 0},
    }
    with open('data.txt', 'w') as f:
        json.dump(data, f)
    print('Счет был сброшен успешно\n')
    score()


game_in_progress = False


def start():
    global game_in_progress
    game_in_progress = True

def restart():
    exec('break')

user_input = ''

commands = ['help', 'menu', 'rules', 'settings', 'start', 'restart', 'score', 'exit', 'delete_score']

map_vals = ''
remaining_vals = ''
move = 0
map = ''
cross = []
zero = []
win_combs = []


def default_values():
    global map_vals, remaining_vals, move, cross, zero
    map_vals = '123456789'
    remaining_vals = '123456789'
    move = 1
    cross = [player1, 'X']
    zero = [player2, 'O']
    if data['settings']['ход'][0] == 'нолики' or (data['settings']['ход'][0] == 'случайный' and roll()):
        cross = [player2, 'X']
        zero = [player1, 'O']
    map_build(map_vals)


def map_build(map_values):
    global map
    map = (map_values[0:3], map_vals[3:6], map_vals[6:10])


def show_map():
    global map
    for strng in map:
        print(strng[0], end='  ')
        print(strng[1], end='  ')
        print(strng[2])


def win_combs_build():
    global win_combs, map_vals
    win_combs = [
        f'{map_vals[0]}{map_vals[1]}{map_vals[2]}',
        f'{map_vals[3]}{map_vals[4]}{map_vals[5]}',
        f'{map_vals[6]}{map_vals[7]}{map_vals[8]}',
        f'{map_vals[0]}{map_vals[3]}{map_vals[6]}',
        f'{map_vals[1]}{map_vals[4]}{map_vals[7]}',
        f'{map_vals[2]}{map_vals[5]}{map_vals[8]}',
        f'{map_vals[0]}{map_vals[4]}{map_vals[8]}',
        f'{map_vals[6]}{map_vals[4]}{map_vals[2]}',
    ]


def player_move(plr, char_, ):
    global map, map_vals, remaining_vals, move

    print(f'{plr}, ваш ход! Выберите куда поставить свой {char_}\n')
    show_map()

    wrong_input = True
    while wrong_input:
        _input()

        if user_input == 'start':
            print('Вы уже в игре. Введите "restart" чтобы начать ее заново')
        elif user_input == 'exit':
            exit()
        elif user_input == 'restart':
            default_values()
            move = 0
            wrong_input = False
        elif user_input in remaining_vals and len(user_input) == 1:
            map_vals = map_vals.replace(user_input, char_)
            remaining_vals = remaining_vals.replace(user_input, '')
            wrong_input = False
        elif user_input in '123456789' and len(user_input) == 1:
            print('Клетка уже занята! Выберите другую')
        elif user_input in commands:
            print('Завершите игру чтобы использовать эту команду')
        else:
            print('Неизвестная ячейка или команда! Напишите "help" чтобы узнать все доступные команды')


def computer_move(char_):
    global map_vals, remaining_vals, data
    time.sleep(1)

    map_build(map_vals)
    _move = random.choice(remaining_vals)
    enemy_char = 'O'
    if char_ == 'O':
        enemy_char = 'X'
    win_combs_build()

    close_win = f'{char_ * 2}'
    close_loose = f'{enemy_char * 2}'

    for comb in win_combs:
        if close_loose in comb * 2:
            potential_move = comb.replace(f'{enemy_char}', '')
            if potential_move in remaining_vals:
                _move = potential_move

    for comb in win_combs:
        if close_win in comb * 2:
            potential_move = comb.replace(f'{char_}', '')
            if potential_move in remaining_vals:
                _move = potential_move

    # для сложности 1 ход заменяеться на случайный, для сложности 2 заменяется в 50% случаях
    if data['settings']['сложность'][0] == '1' or (data['settings']['сложность'][0] == '2' and roll()):
        _move = random.choice(remaining_vals)

    map_vals = map_vals.replace(_move, char_)
    remaining_vals = remaining_vals.replace(_move, '')


def win_check(plr, char_):
    global win_combs, data, game_in_progress, player2

    win_combs_build()

    if any(f'{char_ * 3}' == comb for comb in win_combs):
        show_map()
        print(f'{plr} победил!')
        game_in_progress = False

        if plr == player1 and player2 == 'computer':
            data["score"][f'сложность {data["settings"]["сложность"][0]}']['Побед'] += 1
        elif plr == 'computer':
            data["score"][f'сложность {data["settings"]["сложность"][0]}']['Поражений'] += 1

    elif len(remaining_vals) == 0:
        show_map()
        print('Свободных клеток не осталось и игра заканчивается ничьей')
        game_in_progress = False

        if player2 == 'computer':
            data["score"][f'сложность {data["settings"]["сложность"][0]}']['Ничьих'] += 1


menu()


# todo: проверка на победу
while True:
    _input()
    if user_input == 'restart':
        print('Вы еще не начали игру! Напишите "start" чтобы начать')
    elif user_input in commands:
        exec(f'{user_input}()')
    else:
        print('Неизвестная команда! Напишите "help" чтобы узнать все доступные команды')

    if game_in_progress:
        default_values()


    while game_in_progress:
        if move % 2 == 1:
            player, char = cross
        else:
            player, char = zero

        if player == 'computer':
            computer_move(char)
        else:
            player_move(player, char)
        map_build(map_vals)
        win_check(player, char)
        move += 1
