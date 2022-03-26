my_list = [1, 4, 5, 8, 9, 11, 13, 12]

my_list1 = [x*2 if x % 2 == 0 else None for x in my_list]
# print(my_list1)

my_list2 = [y*2 for y in my_list if y > 12]
# print(my_list2)

list_2 = my_list2[:]
# print(list_2)


def get_images_from_list_download(list_file):
    l_img_only = ['png', 'jpeg', 'jpg']
    return [image for image in list_file if image.endswith(tuple(l_img_only))]


list_download = ['aaaa.xyz', 'bbbb.png', 'ccccc.jpeg', 'dddddd.txt', 'eeeee.jpg']
new_list = get_images_from_list_download(list_download)
# print(new_list)


def get_obj_stl_from_list_download(list_download):
    l_obj_stl_ext = ['obj', 'stl']
    return [file for file in list_download if file.endswith(tuple(l_obj_stl_ext))]


list_download = ['aaaaa.obj', 'bbbbbb.oaa', 'cccc.stl', 'dddddd.stl']
n_list = get_obj_stl_from_list_download(list_download)
print(n_list)
