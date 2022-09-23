
for num1 in range(1, 11):
    if num1 == 1:
        print(f'Умножение на {num1}:')
    else:
        print(f'\n \n Умножение на {num1}:')
    for num2 in range(1, 11):
        print(f'{num1}*{num2}={num1*num2}')
