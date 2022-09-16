
        # Переменные названы соответственно их значению
num_1 = float(input('Enter first number: '))
num_2 = float(input('Enter second number: '))
num_3 = float(input('Enter third number: '))

max = ""

if num_2 < num_1 > num_3 or num_2 == num_1 > num_3 or num_2 < num_1 == num_3 or num_2 == num_1 == num_3:
    max =  num_1
elif num_1 < num_2 > num_3 or num_1 < num_2 == num_3:
    max = num_2
elif num_1 < num_3 > num_2:
    max = num_3
else:
    print('Unknown error')
    exit()

print(max)

        # Переменные названы соответственно условию
# a = float(input('Enter first number: '))
# b = float(input('Enter second number: '))
# c = float(input('Enter third number: '))
#
# max = ""
#
# if b < a > c or b == a > c or b < a == c or b == a == c:
#     max =  a
# elif a < b > c or a < b == c:
#     max = b
# elif a < c > b:
#     max = c
# else:
#     print('Unknown error')
#     exit()
#
# print(max)

