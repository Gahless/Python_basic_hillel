
length = int(input('Задайте длину последовательности фибаначи: '))

helper_1 = 1
helper_2 = 1

while length > 0:

    print(helper_1)
    helper_2 += helper_1
    length -= 1
    if length > 0:
        print(helper_2)
        helper_1 += helper_2
        length -= 1
