#reversing "num"

        #Грязный, но интересный способ
num = int(input('Введите трехзначное число для отзеркаливания: '))

m = num % 10        #вычисляем n,u,m
nu = num - m
u = nu % 100
n = nu - u

n = int(n / 100)            #меняем n и m местами
m *= 100

mun = m + u + n

if num % 1000 == 0:
    print('000') #тут без строки не вывести 0 в начале, но я не провожу с ней операций
elif num % 100 == 0:
    print('00' + str(mun))
elif num % 10 == 0:
    print('0' + str(mun))
else:
    print(mun)

        #Чистый, но скучный способ
# number = int(input('Введите трехзначное число для отзеркаливания: '))
#
# digit_1 = number // 100
# digit_2 = (number // 10) % 10
# digit_3 = number % 10
#
# reversed_number = digit_3 * 100 + digit_2 * 10 + digit_1
#
# if number % 1000 == 0:
#     print('000') #тут без строки не вывести 0 в начале, но я не провожу с ней операций
# elif number % 100 == 0:
#     print('00' + str(reversed_number))
# elif number % 10 == 0:
#     print('0' + str(reversed_number))
# else:
#     print(reversed_number)