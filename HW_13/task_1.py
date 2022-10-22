# В условии не написано что функция возвращает, но написано "функция" а не "процесс"
# так что вернул результат работы

import random


def change(lst: list):
    temp = lst.pop()
    lst.append(lst[0])
    lst[0] = temp
    return lst


test_list = list(random.choices(range(10), k=5))

print(test_list)
print(change(test_list))
