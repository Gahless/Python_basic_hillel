
A = []
C = []
list_size = 5

for i in range(list_size):
    number = float(input(f'Введите число {i + 1}/{list_size}: '))
    if number % 1 == 0:
        number = int(number)
    A.append(number)

for obj in A:
    if obj > 5:
        C.append(obj)

print(f'\nСписок чисел больше 5: {C}')
