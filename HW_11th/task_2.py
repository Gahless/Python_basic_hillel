
# Число файлов + валидатор
base_size_correct = False
base_size = 0
base_dict = dict()
request_list = []
while not base_size_correct:

    base_size = input('Задайте число файлов: ')

    if base_size.isdigit() and int(base_size) > 0:
        base_size = int(base_size)
        base_size_correct = True
    else:
        print('Неверный ввод!\n"Число файлов" должно быть целым положительным числом больше 0\n')

print(f'\nЗадайте {base_size} файлов')
print('Для этого введите "имя_файла_без_пробелов.расширение допустимые запросы заглавными через пробел"')
print('запись – W \nчтение – R \nзапуск – X\n')

# Запрос файлов с операциями, валидация + упаковка их в словарь
for i in range(base_size):

    temp_string_correct = False
    while not temp_string_correct:
        temp_string = input(f'Задайте файл #{i + 1}: ')
        temp_list = temp_string.split()
        if not ('.' in temp_list[0]):
            print('Неправильное имя файла. Попробуйте еще раз')
            continue
        elif len(temp_list) < 2:
            print('Ввод имеет слишком мало элементов. Попробуйте еще раз')
            continue
        elif len(temp_list) > 4:
            print('Ввод имеет слишком много элементов. Попробуйте еще раз')
            continue

        temp_dict_key = temp_list.pop(0)

        # Валидация операций
        wrong_operation = False
        for single_operation in temp_list:
            if single_operation not in 'WRX':
                wrong_operation = True
        if wrong_operation:
            print('Вы ввели недопустимые операции для файла. Попробуйте еще раз')
            continue
        # Упаковка правильного инпута в словарь
        base_dict[temp_dict_key] = temp_list
        temp_string_correct = True


del i
del temp_list
del temp_string
del temp_dict_key

# Запрос числа запросов + валидатор
request_amount = 0
request_amount_correct = False
while not request_amount_correct:

    request_amount = input('\nВведите число запросов: ')

    if request_amount.isdigit() and int(request_amount) > 0:
        request_amount = int(request_amount)
        request_amount_correct = True
    else:
        print('Неверный ввод!\n"Число запросов" должно быть целым положительным числом больше 0')

print(f'\nВведите {request_amount} запросов')
print('Для этого введите "операция и заданный_ранее_файйл.расширение"')
print('Доступные операции: \nwrite \nread \nexecute \n')

# Создание списка запросов

for i in range(request_amount):

    temp_string = input(f'Введите запрос #{i + 1}: ')
    temp_list = temp_string.split()
    # Перевод операций
    if temp_list[0] == 'write':
        temp_list[0] = 'W'
    elif temp_list[0] == 'read':
        temp_list[0] = 'R'
    elif temp_list[0] == 'execute':
        temp_list[0] = 'X'
    else:
        temp_list[0] = 'Unknown request'

    request_list.append(temp_list)


for request in request_list:

    if len(request) == 1:
        print('Access denied! (Запрос имеет слишком мало элементов)')
        continue
    elif len(request) > 2:
        print('Access denied! (Запрос имеет слишком много элементов)')
        continue
    elif request[0] == 'Unknown request':
        print('Access denied! (Неизвестная операция)')
        continue

    request, dict_key = request
    if dict_key not in base_dict:
        print('Access denied! (Неизвестный файл)')
    elif request in base_dict[dict_key]:
        print('Ok')
    else:
        print('Access denied! (Недопустимая операция)')

'дополнительные тестовые значения ниже!!!'

# Тестовые значения:
# 5
# Задайте файл #1: Test.txt W R
# Задайте файл #2: python.py X
# Задайте файл #3: script.exe W R X
# Задайте файл #4: notebook.exe R W X
# Задайте файл #5: book.txt R W
#
# 10
# Введите запрос #1: piss on Test.txt
# Введите запрос #2: miss dark.exe
# Введите запрос #3: read dark.exe
# Введите запрос #4: kiss python.py
# Введите запрос #5: write Test.txt
# Введите запрос #6: write Test.exe
# Введите запрос #7: paramparamtam
# Введите запрос #8: read python.py
# Введите запрос #9: read notebook.exe
# Введите запрос #10: execute python.py
