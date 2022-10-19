
import copy
import json
from typing import Dict, Union

A = {
    'key1.1': 'value1.1',
    'key1.2': 'value1.2',
    'key1.3': 'value1.3',
    'key1.4': 'value1.4',
    'key1.5': 'value1.5',
    'common_key1': 'common_value1.1',
    'common_key2': 'common_value1.2',
    'common_key3': 'common_value1.3',
    'common_key4': 'common_value1.4'
}
B = {
    'key2.1': 'value2.1',
    'key2.2': 'value2.2',
    'key2.3': 'value2.3',
    'key2.4': 'value2.4',
    'key2.5': 'value2.5',
    'common_key1': 'common_value2.1',
    'common_key2': 'common_value2.2',
    'common_key3': 'common_value2.3',
    'common_key4': 'common_value2.4'
}

# Основа третьего словаря - наибольший
C_is_A = False
if len(A) >= len(B):
    C: Dict[str, Union[str, list]] = copy.deepcopy(A)  # Dict чтобы убрать warning
    smaller_dict = copy.deepcopy(B)
    C_is_A = True
else:
    C: Dict[str, Union[str, list]] = copy.deepcopy(B)
    smaller_dict = copy.deepcopy(A)

# Добавление к основе второго словаря так, чтобы чтобы общие значения словаря "А" всегдя были первыми
if C_is_A:
    for key in smaller_dict:
        if key in C:
            C[key] = [C[key], smaller_dict[key]]
            continue
        C[key] = smaller_dict[key]
else:
    for key in smaller_dict:
        if key in C:
            C[key] = [smaller_dict[key], C[key]]
            continue
        C[key] = smaller_dict[key]


with open('task_2.json', 'w') as f:
    f.write(json.dumps(C))


'''
Пытался оптимизировать код как мог
Чтобы к большему словарю добавлялся меньший, но у общих ключей значение первого словаря всегда было первым
Сначала хотел сделать один цикл и запихнуть в него два if-а, но это вызвало бы больше операций чем два цикла под if-ом
но код в итоге вышел в 3 раза больше чем мог бы. Не знаю стоит ли оно того
'''