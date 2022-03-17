my_list = [1, 4, 5, 8, 9, 11, 13, 12]

my_list1 = [x*2 if x % 2 == 0 else None for x in my_list]
print(my_list1)

my_list2 = [y*2 for y in my_list if y > 12]
print(my_list2)

list_2 = my_list2[:]
print(list_2)
