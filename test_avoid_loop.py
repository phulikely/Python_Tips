my_list = [1, 4, 5, 8, 9, 11, 13, 12]

my_list1 = [x*2 if x % 2 == 0 else None for x in my_list]
# print(my_list1)

my_list2 = [y*2 for y in my_list if y > 12]
# print(my_list2)

list_2 = my_list2[:]
# print(list_2)


def get_images_from_list_download(list_file):
    return [image for image in list_file if
            image.endswith('.png') or image.endswith('.jpg') or image.endswith('.jpeg')]


list_download = ['aaaa.xyz', 'bbbb.png', 'ccccc.jpeg', 'dddddd.txt', 'eeeee.jpg']
new_list = get_images_from_list_download(list_download)
print(new_list)
