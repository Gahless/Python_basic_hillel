# Symbol codes:
# eng a-z: 97-122, A-Z: 65-90 (26 letters)
# ru а-я: 1072-1103, А-Я: 1040-1071 (32 letters)
# 0-9: 48-57 (10 "letters")

print('Внимание!!!\nПрограмма обрабатывает только цифры и буквы английского и русского алфавита (кроме "ё")')
print('Разделительные символы, а так же буквы из других алфавитов остаются без изменений\n')
phrase = input('Введите фразу: ')
shift = int(input('Введите размер сдвига: '))

eng_a = 97
eng_z = 122
eng_A = 65
eng_Z = 90
ru_a = 1072
ru_z = 1103         # z = последняя буква алфавита
ru_A = 1040
ru_Z = 1071
zero = 48
nine = 57

range_eng_az = list(range(eng_a, eng_z + 1))    # англ алфавит
range_eng_AZ = list(range(eng_A, eng_Z + 1))    # англ заглав алфавит
range_ru_az = list(range(ru_a, ru_z + 1))       # ру алфавит
range_ru_AZ = list(range(ru_A, ru_Z + 1))       # ру заглав алфавит
range_09 = list(range(zero, nine + 1))          # цифры

for char in phrase:
    code = ord(char)

    if code in range_eng_az:
        start = eng_a
        letters_amount = 26
    elif code in range_eng_AZ:
        start = eng_A
        letters_amount = 26
    elif code in range_ru_az:
        start = ru_a
        letters_amount = 32
    elif code in range_ru_AZ:
        start = ru_A
        letters_amount = 32
    elif code in range_09:
        start = zero
        letters_amount = 10
    else:
        print(char, end='')
        continue

    symbol_number_in_abc = code - start
    processed_symbol_number_in_abc = (symbol_number_in_abc + shift) % letters_amount  # Сдвиг символа + закругление алфавита
    processed_symbol = chr(start + processed_symbol_number_in_abc)

    print(processed_symbol, end='')
