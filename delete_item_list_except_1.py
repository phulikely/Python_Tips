list_test1 = ['aaaa', 'bbbb', 'cccc']
lst_item = list_test1[-1]


for file in list_test1[:]:
    if file is not lst_item:
        list_test1.remove(file)

print(list_test1)