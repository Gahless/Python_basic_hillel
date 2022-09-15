#reversing "num"

num = int(input('Введите трехзначное число для отзеркаливания: '))

digit_1 = num // 100
digit_2 = num // 10 - digit_1 * 10
digit_3 = num - digit_1 * 100 - digit_2 * 10

mun = digit_3 * 100 + digit_2 * 10 + digit_1

print(mun)
