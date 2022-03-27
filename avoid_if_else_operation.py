def create_cube(name=None, width=None, height=None, length=None):
    print(name)
    print(width)
    return 1


def create_sphere(name=None, width=None, height=None, length=None):
    print(f'width is {width} and height is {height}')
    return [1, 2, 3]


def fill_holes(name=None, width=None, height=None, length=None):
    height = height + length
    return height


def smooth(name=None, width=None, height=None, length=None):
    list_test = [name, 'aaa.png', 'bbb.jpg', 'ccc.jpeg', 'dddd.stl', 'FFF.png', length]
    print(list_test[1:2])
    return list_test[-1]


def default_func():
    return 'Incorrect selection'

