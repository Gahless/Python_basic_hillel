
list_1 = []
list_size = 10

for i in range(list_size):
    number = float(input(f'Введите число {i + 1}/{list_size}: '))
    if number % 1 == 0:
        number = int(number)
    list_1.append(number)

N = float(input('\nВведите число для поиска в списке: '))

print('\nЧисло совпадений:', list_1.count(N))
