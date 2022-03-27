from avoid_if_else_operation import *


class UsingDict:
    def __init__(self, action_id, name, width, height, length):
        self.action_id = action_id
        self.name = name
        self.width = width
        self.height = height
        self.length = length

    def show_info_about_selection(self):
        args = dict(name=self.name, width=self.width, height=self.height, length=self.length)
        info_dict = {
            1: lambda: create_cube(**args),
            2: lambda: create_sphere(**args),
            3: lambda: fill_holes(**args),
            4: lambda: smooth(**args)
        }
        return info_dict.get(self.action_id, default_func)()


def main():
    action_id = 4
    name = 'test 123456'
    width = 13579
    height = 2468
    length = 7777
    using_dict = UsingDict(action_id=action_id, name=name, width=width, height=height, length=length)
    result = using_dict.show_info_about_selection()
    print(result)


if __name__ == '__main__':
    main()
