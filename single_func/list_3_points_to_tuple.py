li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
v = iter(li)

li = [(i, next(v), next(v)) for i in v]  # creates list of tuples
print(li)

list_points = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_l = [tuple(i) for i in list_points]
print(new_l)
