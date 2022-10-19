
import copy
import json

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

C_is_A = False
if len(A) >= len(B):
    C = copy.deepcopy(A)
    smaller_dict = copy.deepcopy(B)
    C_is_A = True
else:
    C = copy.deepcopy(B)
    smaller_dict = copy.deepcopy(A)

if C_is_A:
    for key in smaller_dict:
        if key in C:
            C[key] = [C[key], smaller_dict[key]]  # А как это выделение убрать? У меня так и не получилось
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
'''