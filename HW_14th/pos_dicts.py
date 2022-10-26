
def arguments_validate(lst, *positions):
    for pos in positions:  # Валидатор pos (целый int больше 0)
        if (not isinstance(pos, int)) or pos % 1 != 0 or pos < 1:
            raise ValueError('pos expected to be an integer and bigger than 0')

    for el in lst:  # Валидатор элементов lst (только словари, только имеющие ключи position и name)
        if not isinstance(el, dict):
            raise ValueError(f'"{el}" is wrong element in lst),'
                             f'"lst" expected to contain only dictionaries')
        if el.get('position') is None or el.get('name') is None:
            raise ValueError(f'{el} expected to contain key "position" and key "name"')


def el_delete(lst: list, pos='last'):
    if pos == 'last':
        pos = len(lst)
    arguments_validate(lst, pos)

    pos -= 1
    del lst[pos]

    for el in lst[pos:]:
        el['position'] -= 1
    return lst


def el_insert(name, lst: list, pos='last'):
    if pos == 'last':
        pos = len(lst) + 1
    arguments_validate(lst, pos)

    lst.insert(pos - 1, {'name': name, 'position': pos})

    for el in lst[pos:]:
        el['position'] += 1
    return lst


def el_swap(lst: list, pos_1: int, pos_2: int):
    arguments_validate(lst, pos_1, pos_2)

    lst[pos_1 - 1]['name'], lst[pos_2 - 1]['name'] = lst[pos_2 - 1]['name'], lst[pos_1 - 1]['name']

    return lst
