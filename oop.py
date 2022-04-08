# Using classes to create something called objects
# An object is made of attributes and methods
# Attributes represent data about object (ex: name, color, speed, ...)
# Methods represent functionality or tasks that the object can do (ex: change the color, adjust speed...)

class Fruit:
    def __init__(self, name, clr): #parameters
        self.name = name #attribute, local variable
        self.colour = clr  #attribute, local variable
        # Nhung~ variable trong init deu la local variable

    def details(self):  #method
        print(f'my {self.name} is {self.colour}')

apple = Fruit('apple', 'red') #arguments
apple.details()