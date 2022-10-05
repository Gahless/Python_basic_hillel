
list_1 = []
list_size = 5

for i in range(list_size):
    number = float(input(f'Введите число {i + 1}/{list_size}: '))
    if number % 1 == 0:
        number = int(number)
    list_1.append(number)

print(list_1)
