
import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""


length = input('Задайте длину пароля: ')

while not length.isnumeric() or int(length) < 4:
    length = input('Пожалуйста, задаqте натуральное число не меньше 4: ')
length = int(length)


main_length = length // 4
rest_of_length = length % 4

symbols_list = [lower, upper, digits, punctuation]
symbols_pool = symbols_list * main_length
symbols_pool.extend(random.choices(symbols_list, k=rest_of_length))
random.shuffle(symbols_pool)

print('\nВаш пароль:\n')

for case in symbols_pool:
    print(random.choice(case), end='')
