from avoid_if_else_operation import *
from functools import partial


def show_info_about_selection(action_id=None):
    name = "Cube12345"
    width = 10
    info_dict = {
        1: lambda: create_cube(name=name),
        2: lambda: create_sphere(width=width),
        3: lambda: fill_holes(),
        4: lambda: smooth()
    }
    return info_dict.get(action_id, default_func)()


selection_id = show_info_about_selection(action_id=4)
print(selection_id)
