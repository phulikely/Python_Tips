# List of Python tricks from Dan Bader's (realpython.com) newsletter

# ===================================== #

# How to merge two dictionaries (3.5+)
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)
# {'c': 4, 'a': 1, 'b': 3}

# ===================================== #

# How to test flags
x, y, z = 0, 1, 0
if x == 1 or y == 1 or z == 1:
    print('passed')
if 1 in (x, y, z):
    print('passed')

# truthiness only:
if x or y or z:
    print('passed')
if any((x, y, z)):
    print('passed')

# ===================================== #

# How to sort a dictionary by value
d = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
sorted(d.items(), key=lambda x: x[1])
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
sorted(d.items(), key=lambda x: x[0])
[('a', 4), ('b', 3), ('c', 2), ('d', 1)]

# ===================================== #

# Use get() to use default values with dictonaries
name_for_userid = {
    382: 'Alice',
    590: 'Bob',
    951: 'Mary'
}
def greeting(userid):
    print (f"Hi {name_for_userid.get(userid, 'there')}!")
greeting(951)
# Hi Mary!
greeting(55555555)
# Hi there!

# ===================================== #

# How to use namedtuples
from collections import namedtuple
Car = namedtuple('Car', 'color mileage')
my_car = Car('red', 12345.6)
print(my_car.color)
# red
print(my_car)
# Car(color='red', mileage=12345.6)

# like tuples, namedtuples are immutable
my_car.color = 'pink'
# AttributeError: can't set attribute

# ===================================== #

# Function argument unpacking
def myfunc(x, y, z):
    print(x + y + z)

tuple_vec = (1, 2, 3)
dict_vec = {'x': 4, 'y': 5, 'z': 6}

print(myfunc(*tuple_vec))
# 6
print(myfunc(**dict_vec))
# 15

# ===================================== #

# Shorthand for swapping variables
a, b = b, a

# ===================================== #

# "is" vs "=="
# "is" expressions evaluate to True if two variables point to the same object
# "==" evaluates to True if the objects referred to by the variables are equal
a = [1, 2, 3]
b = a
c = list(a)

a == b
# True
a is b
# True

a == c
# True
a is c
# False

# ===================================== #

# Functions are first-class citizens
# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures

def myfunc(a, b):
    return a + b
funcs = [myfunc]
print(funcs[0])
# <function myfunc at 0x000001C8E48C5AB0>
print(funcs[0](2, 3))
# 5

# ===================================== #

# Use functions to emulate a switch block
def endless_if_else(operator, x ,y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None

def avoid_if_else(operator, x, y):
    return{
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

print(endless_if_else('mul', 2, 8))
# 16
print(avoid_if_else('mul', 2, 8))
# 16
print(endless_if_else('AAAAAAAAA', 2, 8))
# None
print(avoid_if_else('AAAAAAAAAAA', 2, 8))
# None

# ===================================== #

even_squares = [x * x for x in range(10) if not x % 2]
# Viet "x % 2" tuong duong voi "x % 2 != 0" --> Lay ra so le
# Vay nen "not x % 2" se ra so ko phai so le(tuc la so chan)
print(even_squares)
# [0, 4, 16, 36, 64]

# ===================================== #

# Use type annotations for hints
def my_add(a: int, b: int) -> int:
    return a + b

# ===================================== #

# Using list slice syntax makes list manipulation easy
# You can clear all elements from a list:
lst = [1, 2, 3, 4, 5]
del lst[:]
print(lst)
# []

# You can replace all elements of a list without creating a new list object:
a = lst
lst[:] = [7, 8, 9]
print(lst)
# [7, 8, 9]
print(a)
# [7, 8, 9]
print(a is lst)
# True

# You can also create a copy(shallow) of a list:
b = lst[:]
print(b)
# [7, 8, 9]
print(b is lst)
# False

# ===================================== #

# Find most common elements in an iterable(list, dict, etc..)
import collections
c = collections.Counter('helloworld')
print(c)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1})
print(c.most_common(3))
# [('l', 3), ('o', 2), ('h', 1)]

# ===================================== #

# Get all permutations from an iterable (list, dict, etc.)
import itertools
for p in itertools.permutations('ABCD'):
  print(p)
"""
('A', 'B', 'C', 'D')
('A', 'B', 'D', 'C')
('A', 'C', 'B', 'D')
('A', 'C', 'D', 'B')
('A', 'D', 'B', 'C')
('A', 'D', 'C', 'B')
('B', 'A', 'C', 'D')
('B', 'A', 'D', 'C')
('B', 'C', 'A', 'D')
('B', 'C', 'D', 'A')
('B', 'D', 'A', 'C')
('B', 'D', 'C', 'A')
('C', 'A', 'B', 'D')
('C', 'A', 'D', 'B')
('C', 'B', 'A', 'D')
('C', 'B', 'D', 'A')
('C', 'D', 'A', 'B')
('C', 'D', 'B', 'A')
('D', 'A', 'B', 'C')
('D', 'A', 'C', 'B')
('D', 'B', 'A', 'C')
('D', 'B', 'C', 'A')
('D', 'C', 'A', 'B')
('D', 'C', 'B', 'A')
"""

# ===================================== #

# @classmethod vs @staticmethod vs "plain" methods
class MyClass:
  def method(self):
    """
    Instance methods need a class instance and
    can access the instance through `self`.
    """
    return 'instance method called', self

  @classmethod
  def classmethod(cls):
    """
    Class methods don't need a class instance.
    They can't access the instance (self) but
    they have access to the class itself via `cls`.
    """
    return 'class method called', cls

  @staticmethod
  def staticmethod():
    """
    Static methods don't have access to `cls` or `self`.
    They work like regular functions but belong to
    the class's namespace.
    """
    return 'static method called'

# All methods types can be called on a class instance:
obj = MyClass()
print(obj.method())
# ('instance method called', <MyClass instance at 0x1019381b8>)
print(obj.classmethod())
# ('class method called', <class MyClass at 0x101a2f4c8>)
print(obj.staticmethod())
# 'static method called'

# Calling instance methods fails if we only have the class object:
print(MyClass.classmethod())
# ('class method called', <class MyClass at 0x101a2f4c8>)
print(MyClass.staticmethod())
# 'static method called'
# print(MyClass.method())
"""
TypeError: 
    "unbound method method() must be called with MyClass "
    "instance as first argument (got nothing instead)"
"""

# ===================================== #

# In Python 3.4+ you can use
# contextlib.suppress() to selectively
# ignore specific exceptions:

import contextlib
import os

with contextlib.suppress(FileNotFoundError):
  os.remove('somefile.tmp')

# This is equivalent to:

try:
  os.remove('somefile.tmp')
except FileNotFoundError:
  pass

# contextlib.suppress docstring: 
#
# "Return a context manager that suppresses any 
#  of the specified exceptions if they occur in the body
#  of a with statement and then resumes execution with 
#  the first statement following the end of 
#  the with statement."

# ===================================== #

