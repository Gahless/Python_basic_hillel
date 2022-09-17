N = int(input('Задайте ширину треугольника: '))
helper = 0
helper2 = N
while helper < N:
    print(' ' * helper + '*' * helper2)
    helper += 1
    helper2 -= 2