matrix = [
[1, 6, 8, 5, 4, 0, 3],
[5, 7, 8, 9, 4, 2, 1],
[6, 0, 7, 8, 1, 2, 5],
[5, 7, 2, 7, 5, 2, 1]
]

high = len(matrix)

for y, y_value in enumerate(matrix):
    for x, x_value in enumerate(y_value):
        if x % 2 == 0 and matrix[0][x] > matrix[(len(matrix)-1)][x]:
            print(x_value, end=' ')
    print('')