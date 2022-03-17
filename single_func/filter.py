"""
filter apply a filter to a list and return items that satisfied the conditions
"""
x = [1, 2, 3, 4, 5, 6, 7]


def filter_pos(x):
    return x > 5 and x % 2 == 0


a = list(filter(filter_pos, x))
print(a)
