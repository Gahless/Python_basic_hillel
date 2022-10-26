import pos_dicts

data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
    {'name': 'Test 4', 'position': 4},
    {'name': 'Test 5', 'position': 5},
]

print(pos_dicts.el_delete(data, 2))
print()
print(pos_dicts.el_insert('Test 2', data, 2))
print()
print(pos_dicts.el_swap(data, 1, 5))
print()
print(pos_dicts.el_delete(data))
print()
print(pos_dicts.el_insert('Test 6', data))
print()
print(pos_dicts.el_insert('Test 7', data))
