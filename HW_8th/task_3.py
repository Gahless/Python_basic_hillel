input_1 = input('Введите пароль проверки: ')

punctuation_list = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

punctuation = 0
digit = 0
upper = 0
more_than_10 = 0

if len(input_1) > 10:
    more_than_10 = 1

for symbol in input_1:

    if symbol in punctuation_list:
        punctuation = 1
    if symbol.isdigit():
        digit = 1
    if symbol.isupper():
        upper = 1


grade = punctuation + digit + upper + more_than_10 + 1
if input_1 in 'admin012345678909876543210qwerty123qwertyasdfghzxcvbnbvcxzhgfdsaytrewq':
    grade = 1
print(f'сложность вашего пароля по шкале от 1 до 5: {grade}')
