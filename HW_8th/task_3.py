input_1 = input('Введите пароль проверки: ')

punctuation_list = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

punctuation = 0
digit = 0
upper = 0
lower = 0
more_than_8 = 0
grade = 0

if len(input_1) > 8:
    more_than_8 = 1

for symbol in input_1:

    if symbol in punctuation_list:
        punctuation = 1
    if symbol.isdigit():
        digit = 1
    if symbol.isupper():
        upper = 1
    if symbol.islower():
        lower = 1

#
conditions = punctuation + digit + upper + lower
if input_1 in 'admin' or input_1 in 'qwerty' or input_1 in '01234567890':
    grade = 1
elif conditions == 4 and more_than_8 == 1:  # Все условия
    grade = 5
elif conditions < 4:  # Три условия
    grade = conditions + 1
else:  # 4 условия
    grade = 4
print(f'Сложность вашего пароля по шкале от 1 до 5: {grade}')
