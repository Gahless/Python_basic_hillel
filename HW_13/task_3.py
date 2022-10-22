
def sum_range(start: int, end: int = 0):

    if start > end:
        return sum(range(end, start + 1))
    return sum(range(start, end + 1))


print(sum_range(5))

