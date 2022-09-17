N = int(input('Задайте ширину треугольника: '))
helper = 0
helper2 = N
while helper * 2 < N:
    print('  ' * helper + '* ' * helper2)
    helper += 1
    helper2 -= 2
if N % 2 ==0 and helper * 2 >= N:
    print('  ' * (helper - 1) + ' ' + '*')