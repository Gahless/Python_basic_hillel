
import random

char_list = list(range(32, 127))

length = int(input('Задайте длину пароля: '))

while length > 0:
    print(chr(random.choice(char_list)), end='')
    length -= 1
    