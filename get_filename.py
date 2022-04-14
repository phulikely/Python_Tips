import os

file_with_path = r"C:\Users\Phulikely\Desktop\test.aaaa.txt"

pathname, extension = os.path.splitext(file_with_path)
filename = pathname.split('\\')
 
print(filename[-1]) #test.aaaa


file_name = "myfile.tar.xyz"
# index = file_name.index('.')
# file_name = file_name[:index]
# print(file_name)
n_f_name = file_name[:-4]
print(n_f_name) #myfile.tar