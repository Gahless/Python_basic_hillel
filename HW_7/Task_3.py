
from random import *

num = randint(1,10)
count = 0
print('Я загадал число от 1 до 10 (включительно). Попробуй угадай за три попытки ;)\n')

while count != 3:
    count += 1
    guess = int(input(f'Попытка #{count}: '))
    if guess == num:
        print('Ты угадал!')
        break
    elif count == 3:
        print(f'\nУвы, ты потратил все попытки. Загаданным числом было "{num}"\nУдачи в следующий раз!')
    elif guess > num:
        print('Бери меньше')
    elif guess < num:
        print('Бери больше')
