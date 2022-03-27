from avoid_if_else_operation import *
from functools import partial


def main():
    action_id = 2
    name = 'test22222'
    width = 1357
    height = 2468
    length = 7777
    show_info_about_selection(action_id=action_id, name=name, width=width, height=height, length=length)


def show_info_about_selection(action_id=0, name='', width=0, height=0, length=0):

    info_dict = {
        1: lambda: create_cube(name=name, width=width),
        2: lambda: create_sphere(width=width, height=height),
        3: lambda: fill_holes(height=height, length=length),
        4: lambda: smooth(length=length, name=name)
    }
    return info_dict.get(action_id, default_func)()


main()
