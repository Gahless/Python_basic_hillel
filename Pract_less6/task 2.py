A = int(input('Введите число "А"'))
B = int(input('Введите число "B"'))

summ = 0

while A < B:
    if A % 2 == 0:
        summ += A
    A += 1

print('Итог :', summ)


#test version
# A = int(input('Введите число "А"'))
# B = int(input('Введите число "B"'))
#
# summ = 0
#
# while A < B:
#     if A % 2 == 0:
#         print(A)
#         summ += A
#         print('   summ =', summ)
#     A += 1
#
# print('Итог :', summ)
