
def read_last(lines: int, file: str):

    if lines % 1 != 0 or lines < 1:
        raise Exception(f'{lines} (lines) expected to be a natural number')

    with open(file) as f:
        all_strings = f.readlines()
        strings_count = len(all_strings)
        for i in range(lines, 0, -1):
            print(all_strings[strings_count - i], end='')


read_last(10, 'task_4.txt')
