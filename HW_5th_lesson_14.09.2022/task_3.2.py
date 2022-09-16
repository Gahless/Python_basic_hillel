#reversing number

    #Грязный, но интересный способ
number = int(input('Введите шестизначное число для отзеркаливания: '))

n = number // 100000
u = (number // 10000) % 10
m = (number // 1000) % 10
b = (number // 100) % 10
e = (number // 10) % 10
r = number % 10

n = n
u *= 10
m *= 100
b *= 1000
e *= 10000
r *= 100000

rebmun = r + e + b + m + u + n

if number % 1000000 == 0:
    print('000000')
elif number % 100000 == 0:
    print('00000', rebmun, sep = '')
elif number % 10000 == 0:
    print('0000', rebmun, sep = '')
elif number % 1000 == 0:
    print('000', rebmun, sep = '')
elif number % 100 == 0:
    print('00', rebmun, sep = '')
elif number % 10 == 0:
    print('0', rebmun, sep = '')
else:
    print(rebmun)


      # Чистый но скучный способ
# number = int(input('Введите шестизначное число для отзеркаливания: '))
#
# digit_1 = number // 100000
# digit_2 = (number // 10000) % 10
# digit_3 = (number // 1000) % 10
# digit_4 = (number // 100) % 10
# digit_5 = (number // 10) % 10
# digit_6 = number % 10
#
# reversed_number = digit_6 * 100000 + digit_5 * 10000 + digit_4 * 1000 + digit_3 * 100 + digit_2 * 10 + digit_1
#
# if number % 1000000 == 0:
#     print('000000')
# elif number % 100000 == 0:
#     print('00000', reversed_number, sep = '')
# elif number % 10000 == 0:
#     print('0000', reversed_number, sep = '')
# elif number % 1000 == 0:
#     print('000', reversed_number, sep = '')
# elif number % 100 == 0:
#     print('00', reversed_number, sep = '')
# elif number % 10 == 0:
#     print('0', reversed_number, sep = '')
# else:
#     print(reversed_number)
