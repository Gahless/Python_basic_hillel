
string = input('Задайте строку для проверки на количество чисел: ')

number_count = 0
previous_symbol = ''
second_previous_symbol = ''
for symbol in string:   # number_count += 1 за первую цифру каждого числа (даже дробного)
    if symbol.isdigit() and not (previous_symbol.isdigit() or (previous_symbol == '.' and second_previous_symbol.isdigit())):
        number_count += 1

    second_previous_symbol = previous_symbol
    previous_symbol = symbol

print(f'количество чисел в строке: {number_count}')
