list_download = ['yellow monkey.obj', 'a3db2568685b4099a057c16539b1bba3_15042022064828.stl', 'yellow monkey.mtl']
list_download = str(list_download)


# def string_to_list(txt):
#     txt = txt.replace('[', '').replace(']', '').replace("'", "")
#     txt = txt.split(',')
#     return remove_space_in_1st_idx(_list=txt)
#     # return txt


# def remove_space_in_1st_idx(_list):
#     print(_list)
#     new_list = []
#     for item in _list:
#         first_idx = item[0]
#         if first_idx == ' ':
#             item = item[1:]
#         new_list.append(item)
#     return new_list      

# aaa = string_to_list(list_download)
# print(aaa)

def string_to_list(txt):
    txt = txt.replace('[', '').replace(']', '').replace("'", "")
    txt_l = txt.split(',')
    return [item[1:] if item[0] == ' ' else item for item in txt_l]

hhh = string_to_list(list_download)
print(hhh)