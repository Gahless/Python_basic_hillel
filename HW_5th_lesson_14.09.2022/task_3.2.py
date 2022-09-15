#reversing number

number = int(input('Введите шестизначное число для отзеркаливания: '))

digit_1 = number // 100000
digit_2 = number // 10000 - digit_1 * 10
digit_3 = number // 1000 - digit_1 * 100 - digit_2 * 10
digit_4 = number // 100 - digit_1 * 1000 - digit_2 * 100 - digit_3 * 10
digit_5 = number // 10 - digit_1 * 10000 - digit_2 * 1000 - digit_3 * 100 - digit_4 * 10
digit_6 = number - digit_1 * 100000 - digit_2 * 10000 - digit_3 * 1000 - digit_4 * 100 - digit_5 * 10

rebmun = digit_6 * 100000 + digit_5 * 10000 + digit_4 * 1000 + digit_3 * 100 + digit_2 * 10 + digit_1

print(rebmun)
