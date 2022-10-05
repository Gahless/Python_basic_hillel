
list_1 = []

N = input('Задайте размер списка: ')
while not N.isdigit():
    N = input('Задайте размер списка (натуральное число): ')
N = int(N)

for i in range(N):
    number = float(input(f'Введите число {i + 1}/{N}: '))
    if number % 1 == 0:
        number = int(number)
    list_1.append(number)

list_1.reverse()
print(f'\nВаш список в обратном порядке: {list_1}')
