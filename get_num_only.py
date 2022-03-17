import re

list_loc = [[10.123, 20, 30.555999], [-40.555, 50, 60]]
list_loc = str(list_loc)
only_number_list = [float(s) for s in re.findall(r'-?\d+\.?\d*', list_loc)]
# print(only_number_list)

list1 = only_number_list[0:3]
list2 = only_number_list[3:6]
print(list2)
