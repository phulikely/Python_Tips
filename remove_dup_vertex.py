list_v = [[1, 2, 3], [2, 3, 4], [5, 6, 7], [8, 9, 9], [8, 9, 9]]

list_v = [t for t in (set(tuple(i) for i in list_v))]
print(list_v)