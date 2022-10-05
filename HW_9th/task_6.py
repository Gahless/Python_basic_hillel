
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

min = list_1[0]
max = list_1[0]

for obj in list_1:
    if obj > max:
        max = obj
    if obj < min:
        min = obj

print(f'\nНаибольшее число: {max}\nНаименьшее число: {min}')
