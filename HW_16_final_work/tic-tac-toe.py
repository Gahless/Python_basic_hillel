import time
import json
import random
import os

with open('data.txt', 'r') as f:
    data = json.load(f)


def roll():
    return random.random


def clear():
    os.system('clear')


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
вертикалиили горизонтали''')


def help():
    print('''Список всех команд:
help - показать все команды
menu - вернуться в начальное меню
rules - правила игры
settings - настройка игры
start - начать игру
restart - перезапустить игру
score - показать счет с компьютером
delete - обнулить счет с компьютером
exit - закрыть программу
''')


def settings():
    global data
    for key in data['settings']:
        print(f'{key}: {data["settings"][key]}')
    print('\nЧто желаете изменить? ("help" для посмотра всех команд)')


def settings_change():
    pass  # todo


game_in_progress = False


def start():
    global game_in_progress
    game_in_progress = True


user_input = ''


def _input():
    global user_input
    user_input = input('>>>')
    user_input = user_input.lower()


commands = ['help', 'menu', 'rules', 'settings', 'start', 'restart', 'score', 'exit']

sett = {
    'число игроков': '1',
    'сложность': '2',
    'ход': 'случайный'  # todo: крестики нолики
}


map_vals = ''
remaining_vals = ''
move = 0
map = ''
cross = []
zero = []
win_combs = []


def default_values():
    global map_vals, remaining_vals, move
    map_vals = '123456789'
    remaining_vals = '123456789'
    move = 1


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


def player_move(plr, char_,):
    global map, map_vals, remaining_vals

    print(f'{plr}, ваш ход! Выберите куда поставить свой {char_}\n')
    show_map()

    wrong_input = True
    while wrong_input:
        _input()
        clear()

        if user_input == 'start':
            print('Вы уже в игре. Введите "restart" чтобы начать ее заново')
        elif user_input in remaining_vals and len(user_input) == 1:
            map_vals = map_vals.replace(user_input, char_)
            remaining_vals = remaining_vals.replace(user_input, '')
            wrong_input = False
        elif user_input in '123456789' and len(user_input) == 1:
            print('Клетка уже занята! Выберите другую')
        elif user_input in commands:
            exec(f'{user_input}()')
        else:
            print('Неизвестная ячейка или команда! Напишите "help" чтобы узнать все доступные команды')


def computer_move(char_):
    global map_vals, remaining_vals, data
    time.sleep(1)
    clear()

    _move = random.choice(remaining_vals)
    enemy_char = 'O'
    if char == 'O':
        enemy_char = 'X'

    close_win = f'{char_*2}'
    close_loose = f'{enemy_char*2}'

    for comb in win_combs:
        if close_loose in comb*2:
            _move = comb.replace(f'{enemy_char}', '')
            break

    for comb in win_combs:
        if close_win in comb*2:
            _move = comb.replace(f'{char_}', '')
            break

    # для сложности 1 ход заменяеться на случайный, для сложности 2 заменяется в 50% случаях
    if data['settings']['сложность'] == '1' or (data['settings']['сложность'] == '2' and roll()):
        _move = random.choice(remaining_vals)

    map_vals = map_vals.replace(_move, char)
    remaining_vals = remaining_vals.replace(_move, '')


def win_check(plr, char_):
    global win_combs, data, game_in_progress

    result = ''

    if any(f'{char_*3}' == comb for comb in win_combs):
        print(f'{plr} победил!')
        game_in_progress = False

        if plr == 'computer':
            result = 'comp'
        else:
            result = 'player'

    elif len(remaining_vals) == 0:
        print('Свободных клеток не осталось и игра заканчивается ничьей')

        result = 'draw'

    if 



player1 = data['player1']
player2 = data['player2']
if sett['число игроков'] == '1':
    player2 = 'Computer'

# todo: проверка на победу
while True:
    _input()
    if user_input == 'restart':
        print('Вы еще не начали игру! Напишите "start" чтобы начать')
    elif user_input in commands:
        exec(f'{user_input}()')
    else:
        print('Неизвестная команда! Напишите "help" чтобы узнать все доступные команды')

    clear()

    if game_in_progress:
        default_values()

        cross = [player1, 'X']
        zero = [player2, 'O']
        if sett['ход'] == 'нолики' or sett['ход'] == 'случайный' and roll():
            cross = [player2, 'X']
            zero = [player1, 'O']

    while game_in_progress:
        if move % 2 == 1:
            player, char = cross
        else:
            player, char = zero

        if player == 'computer':
            computer_move(char)
        else:
            player_move(player, char)

