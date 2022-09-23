
N = int(input('Задайте ширину треугольника "N": '))

char = '*'


print('1)')
char_number = N
while char_number != 0:
    print(char * char_number)
    char_number -= 1


print('2)')
char_number = 0
while char_number != N:
    char_number += 1
    print(char * char_number)


print('3)')
char_number = N
space_number = 0
while char_number != 0:
    print(' ' * space_number + char * char_number)
    space_number += 1
    char_number -= 1


print('4)')
char_number = 0
space_number = N - 1
while char_number != N:
    char_number += 1
    print(' ' * space_number + char * char_number)
    space_number -= 1
