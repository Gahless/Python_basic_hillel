
matrix = [
[1, 6, 8, 5, 4, 0, 3],
[5, 7, 8, 9, 4, 2, 1],
[6, 0, 7, 8, 1, 2, 5],
[5, 7, 2, 7, 5, 2, 1]
]

high = len(matrix)

for y in range(high):
    print(matrix[y][0], matrix[y][(len(matrix[y])-1)])