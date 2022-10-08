
print('Добро пожаловать в игру "Крестики-нолики"!!!\n')
player_1 = input('Игрок1, введите свой ник: ')
print(f'Отлично!! {player_1}, вы будете играть за КРЕСТИКИ')
player_2 = input('\nИгрок2, введите свой ник: ')
print(f'Отлично!! {player_2}, вы будете играть за НОЛИКИ')
print('\nИ так, НАЧИНАЕМ!')

default_map = [
     ['1', '2', '3'],
     ['4', '5', '6'],
     ['7', '8', '9']
]
map = [
     ['1', '2', '3'],
     ['4', '5', '6'],
     ['7', '8', '9']
]
final_result = None
y = 0
x = 0
move_count = 1
move_belongs_player = ''
move_belongs_text = ''
move_belongs_char = ''
odd_move = [player_1, 'КРЕСТИК', 'X']
even_move = [player_2, 'НОЛИК', 'O']

while final_result == None:

    if move_count % 2 == 0:
        move_belongs_player, move_belongs_text, move_belongs_char = even_move
    else:
        move_belongs_player, move_belongs_text, move_belongs_char = odd_move

    print(f'\nИгрок "{move_belongs_player}", ваш ход. Выберите номер ячейки куда поставите свой {move_belongs_text}')

    for y in map:
        print(y)

    proper_move = False
    while not proper_move:
        move = input(f'Я ставлю свой {move_belongs_text} в ячейку под номером: ')
        
        if not move.isdigit():
            print('Вы должны ввести натуральное число соответствующее номеру ячейки')
            continue
        if int(move) not in range(1, 10):
            print('Вы должны ввести число соответствующее номеру ячейки')

        cell_found = False
        for y, y_value in enumerate(default_map):
            for x, x_value in enumerate(y_value):
                if x_value == move:  # Находим индекс выбраной ячейки
                    cell_found = True
                    break
            if cell_found:
                break
        
        if map[y][x] == move:  # Проверяем имеет ли ячейка начальное значение, или уже занята
            proper_move = True
        else:
            print('Похоже что эта ячейка уже занята, выбери другую')
            
    map[y][x] = move_belongs_char
            
    win_ways = []
    for i_1 in range(3):
        temp_i_12 = []
        temp_i_21 = []
        for i_2 in range(3):
            temp_i_12.append(map[i_1][i_2])
            temp_i_21.append((map[i_2][i_1]))
        win_ways.append(temp_i_12)  # горизонтальные линии
        win_ways.append(temp_i_21)  # вертикальные линии
    win_ways.append([map[0][0], map[1][1], map[2][2]])  # диагональ 1
    win_ways.append([map[2][0], map[1][1], map[0][2]])  # диагональ 2

    win = [move_belongs_char, move_belongs_char, move_belongs_char]
    if any(win == win_way for win_way in win_ways):
        final_result = f'\n\nПобедил игрок "{move_belongs_player}" с символом {move_belongs_text}'

    cell_filled = []
    for y, value_y in enumerate(map):
        for x, value_x in enumerate(value_y):
            cell_filled.append(map[y][x] in 'OX')  # проверка ячеек на заполненость
    if all(cell_filled): # если все ячейки заполнены то ничья
        final_result = f'\n\nИгрок "{move_belongs_player}" занял последнюю ячейку. Игра завершилась ничьей'

    move_count += 1

print(final_result)
print(f'Количество ходов в игре: {move_count}')
    