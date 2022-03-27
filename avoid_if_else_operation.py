def create_cube(name=None, width=None):
    print(name)
    print(width)
    return 1


def create_sphere(width=None, height=None):
    print(f'width is {width} and height is {height}')
    return [1, 2, 3]


def fill_holes(height=None, length=None):
    height = height + length
    return height


def smooth(length=None, name=None):
    list_test = [name, 'aaa.png', 'bbb.jpg', 'ccc.jpeg', 'dddd.stl', 'FFF.png', length]
    print(list_test[-1])
    return list_test[-1]


def default_func():
    return 'Incorrect selection'

