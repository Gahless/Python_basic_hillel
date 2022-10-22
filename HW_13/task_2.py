
def to_dict(lst: list):
    func_dict = dict()
    for value in lst:
        func_dict[value] = value
    return func_dict


test_list = list(range(10))

test_dict = to_dict(test_list)
print(test_dict)
