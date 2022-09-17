
A = int(input('Введите число "А"'))
B = int(input('Введите число "B"'))

A += A #Чтобы А не входило в диапазон
summ = 0

while A < B:
    summ += A
    A += 1

print('Итог :', summ)

# Test version
# A = int(input('Введите число "А"'))
# B = int(input('Введите число "B"'))
#
# A += A
# summ = 0
#
# while A < B:
#     print('num =', A)
#     summ += A
#     print('   summ =', summ)
#     A += 1
#
# print('Итог :', summ)






