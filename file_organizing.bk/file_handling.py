# file handling: navigate, rename, move, copy, remove
import os
from pathlib import Path
import shutil
# print(os.getcwd())  # D:\Python\Tips

os.chdir(r'D:\Python\Tips\file_organizing')
# print(os.getcwd())  # D:\Python\Tips\file_organizing

# print(os.listdir()) # ['.DS_Store', 'file_handling.py', 'test-file-1.txt']

Path('data').mkdir(exist_ok=True)

# file_handling.py
# test_file.py
for file in os.listdir():
    if file == '.DS_Store' or file.endswith('py'):
        continue    # continue for loop, cau lenh phia sau ko dc thuc thi
        # pass      # cau lenh phia sau van dc thuc hien


    """
    # With test_file.py, name is test_file and extension is .py
    # print(f'With {file}, name is {name} and extension is {ext}')
    """
    name, ext = os.path.splitext(file)


    """
    ['test ', ' file', '2']
    ['test', 'file', '1']
    """
    splitted = name.split('-')


    """
    ['test', 'file', '2']
    ['test', 'file', '1']
    """
    splitted = [s.strip() for s in splitted]


    """
    002-file-test.txt
    001-file-test.txt
    """
    new_name = f'{splitted[2].zfill(3)}-{splitted[1]}-{splitted[0]}{ext}'


    os.rename(file, new_name)

    shutil.move(file, 'data')

