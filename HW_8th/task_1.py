
input_1 = input('Введите строку для проверки: ')

space = 0
digit = 0
upper = 0
lower = 0


for symbol in input_1:

    if symbol.isspace():
        space = 1
    if symbol.isdigit():
        digit = 1
    if symbol.isupper():
        upper = 1
    if symbol.islower():
        lower = 1
if space and digit and upper and lower:
    print('YES')
else:
    print('NO')
