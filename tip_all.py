#17 Iterate with enumerate() instead of range(len())
data = [1, 2, -4, -3]
for idx, num in enumerate(data):
	if num < 0:
		data[idx] = 0
print(data) # [1, 2, 0, 0]


#18 Use list comprehensions instead of for raw loops
squares = [i*i for i in range(3)] # [0, 1, 4]


#19 Sort complex iterables with sorted()
data = [3, 5, 1, 10, 9] # also works with tuple (3, 5, 1, 10, 9) but result will be a list
sorted_data = sorted(data, reverse=True)
print(sorted_data) # [10, 9, 5, 3, 1]

data = [{"name": "Max", "age": 6},
		{"name": "Lisa", "age": 20},
		{"name": "Ben", "age": 9}]
sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data) # [{"name": "Max", "age": 6},{"name": "Ben", "age": 9},{"name": "Lisa", "age": 20}]


#20 Store unique values with Sets
my_list = [1, 2, 3, 4, 5, 6, 7, 7, 7]
my_set = set(my_list)
print(my_set) # {1, 2, 3, 4, 5, 6, 7}


#21 Save memory with Generators
import sys
my_gen = (i for i in range(10000))
print(sum(my_gen)) # 49995000
print(sys.getsizeof(my_gen), "bytes") # 128 bytes


#22 Define default values in Dictionaries with .get() and .setdefault()
my_dict = {"item": "footbal", "price": 10.00}
count = my_dict.get("count") # None
count = my_dict.get("count", 0) # 0
count = my_dict.setdefault("count", 0)
print(count) # 0
print(my_dict) # {'item': 'footbal', 'price': 10.00, 'count': 0}


#23 Count hashable objects with collections.Counter
from collections import Counter
my_list = [10, 10, 10, 5, 5, 2, 9, 9, 9, 9, 9, 9]
counter = Counter(my_list)
print(counter) # Counter({9: 6, 10: 3, 5: 2, 2: 1})
print(counter[10]) # 3
print(counter[11]) # 0
most_common = counter.most_common(2)
print(most_common) # [(9, 6), (10, 3)]
most_common = counter.most_common(1)
print(most_common) # [(9, 6)]
print(most_common[0]) # (9, 6)
print(most_common[0][0]) # 9


# 24 Format strings with f-string
name = "Alex"
my_string = f"Hello {name}"
print(my_string) # Hello Alex

i = 10
print(f'{i} squared is {i*i}')


#25 Concat string with .join()
list_of_strings = ["Hello", "my", "friend"]
my_string = " ".join(list_of_strings)
print(my_string) # Hello my friend


#26 Merge two dictionaries
d1 = {"name": "Alex", "age": 25}
d2 = {"name": "Alex", "city": "New York"}
merged_dict = {**d1, **d2}
print(merged_dict) # {'name': 'Alex', 'age': 25, 'city': 'New York'}


#27 Simplify if-statement with if x in [a, b, c]
colors = ["red", "green", "blue"]
c == "red"
if c in colors:
	print("is main color")
	

#28 Use any instead of loop
numbers = [-1, -2, -4, 0, 3, -7]
has_positives = any(n > 0 for n in numbers)
print(has_positives) # True


#29 Replace if statement with if expression
x = 1 if condition else 2


#30 
if currency == "USD" or currency == "EUR":	############# Bad
	do_something
else:
	do_something

if currency in ["USD", "EUR"]:				############# Better
	do_something
else:
	do_something


# 31 Merge append into list declaration
players = []
players.append("Patrick")		############# Bad
players.append("Max")			############# Bad
players.append("Jessi")			############# Bad

players = ["Patrick", "Max", "Jessi"]	############# Better


#32 Use items() to directly unpack dictionary values
teams_by_color = {"blue": ["Patrick", "Jessi"]}
for team_color, players in teams_by_color.items():
	if condition:
		do_something


#1 Using Unpacking to Write Concise Code
a, b = 2, 'my-string'
a, b = b, a

x = (1, 2, 4, 8, 16)
a, b, c, d, e = x
#######################################


#2 Using Chaining to Write Concise Code
x = y = z = 2
>>> x, y, z
(2, 2, 2)


#3 Checking against None
x, y = 2, None
>>> x is None
False
>>> y is None
True
>>> x is not None
True


#4 Iterating over Sequences and Mappings
x = [1, 2, 4, 8, 16]
y = 'abcde'

for item in reversed(x):
	print(item)

for i, item in enumerate(x):
	print(i, item)
0 1
1 2
2 4
3 8
4 16

for item in zip(x, y):
	print(item)
(1, 'a')
(2, 'b')
(4, 'c')
(8, 'd')
(16, 'e')


#5 Comparing to Zero
x = (1, 2, 0, 3, 0, 4)
# The Pythonic way is to exploit the fact that zero is interpreted as False in a Boolean context, 
# while all other numbers are considered as True
for item in x:
	if item: # item != 0
		print(item)
1
2
3
4


#6 Avoiding Mutable Optional Arguments
>>> def f(value, seq=None):
...     if not seq:
...         seq = []
...     seq.append(value)
...     return seq


#7 Using Context Managers to Release Resources
>>> with open('filename.csv', 'w') as my_file:
...     # do something with `my_file`


#8 Use the Falsy & Truthy Concepts
(x, y) = (True, 0)
# x is truthy
if x:
  # do something
else:
  # do something else
# y is falsy
if not y:
  # do something
ls = [2, 5]
if ls:
  # do something


#9 Ternary Operator replacement
a = True
value = 1 if a else 0
print(value)


#10 Use the ‘in’ keyword
city = 'Nairobi'
found = city in {'Nairobi', 'Kampala', 'Lagos'} # found = True


#11 Sets
ls1 = [1, 2, 3, 4, 5]
ls2 = [4, 5, 6, 7, 8]
elements_in_both = list( set(ls1) & set(ls2) )
print(elements_in_both)


#12 Set Comprehension
elements = [1, 3, 5, 2, 3, 7, 9, 2, 7]
unique_elements = set(elements)
print(unique_elements)


# Use the default parameter of ‘dict.get’ to provide default values
auth = payload.get('auth_token', 'Unauthorized') # auth = payload['auth_token'] if 'auth_token' in payload else auth = 'Unauthorized'


#13 Don’t Repeat Yourself (DRY)
if user:
  print('{0}\n{1}\n{0}'.format('-'*30, user))

if user:
  print('------------------------------')
  print(user)
  print('------------------------------')


#14 Prefer list comprehension over loops
newlist = [i**2 for i in range(1, 100) if i%2==0]


#15 Proper import
from math import sqrt
value = sqrt(50)


#16 String Concatenation
output = " ".join(["Programming" , "is", "fun"])


#33 Create list of tuple from given coordinates
li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
v = iter(li)

li = [(i, next(v), next(v)) for i in v]  # creates list of tuples
print(li) # [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18)]

list_points = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_l = [tuple(i) for i in list_points]
print(new_l) # [(1, 2, 3), (4, 5, 6), (7, 8, 9)]


#34 Get number only from list string
import re

list_loc = [[10.123, 20, 30.555999], [-40.555, 50, 60]]
list_loc = str(list_loc)
only_number_list = [float(s) for s in re.findall(r'-?\d+\.?\d*', list_loc)]
print(list2) # [10.123, 20.0, 30.555999, -40.555, 50.0, 60.0]


#35 Dictionary
dic = {"a": 1, "b": 2}
a, b = dic
print(a, b) #a b
c, d = dic.item()
print(c, d) #1 2


#36 *args and **kwargs
def func1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

args = [1, 2, 3]
func1(**args)


def func2(arg1=None, arg2=None, arg3=None):
    print(arg1, arg2, arg3)

kwargs = {"arg2": 2, "arg1": 1, "arg3": 3}
func2(*args) # arg2 arg1 arg3   #key
func2(**args) # 1 2 3           #value


#37 For else & While else
search = [1, 2, 3, 4, 5, 6, 7]
target = 7

for item in search:
    if item == target:
        print('I found it!')
        break
else:
    print("I didn't find it!")

i = 0
while i < len(search):
    item = search[i]
    if item == target:
        print('I found it!')
        break
    i += 1
else:
    print("I didn't find it!")


# 38 Suppress scientific notation
1.00000e-05
>>> f'{a:.20f}'
'-0.00000000000000007186'


#39 If else in one line
var = 42 if 3>2 else 9
print(var)


#40 Print without new lines
data = [0, 1, 2, 3, 4, 5]
print(*data)    # 0 1 2 3 4 5


#41 Day left in year
import datetime;print((datetime.data(2022,12,31)-datetime.date.today()).days)


#42 Reverse a list
a = [1, 2, 3, 4, 5, 6]
a = a[::-1]
print(a)    #[6, 5, 4, 3, 2, 1]

b = 'level'
b = b[::-1]
print(b)    #level
print(b == b[::-1]) #True


#43 Space separated numbers to int list
user_input = "1 2 3 4 5 6"
my_list = list(map(int, user_input.split()))
print(my_list)  #[1, 2, 3, 4, 5, 6]


#44 Read file into list
names = [line.strip() for line in open('names.txt', 'r')]
print(names)    #['Jessi', 'Robin', 'Mary', 'Tom', 'PAA']


#45 Use sum in a loop
numbers = [10, 20, 30, 40, 50]
result = sum(numbers)
print(result)   #150


#46 Use enumerate
numbers = [10, 20, 33, 40]
for idx, val in enumerate(numbers, start=1):
    print(idx, val) #1  10
                    #2  20
                    #3  33
                    #4  40


#47 Use zip
a = [1, 2, 3, 4]
b = ['a', 'b', 'c']
for val1, val2 in zip(a, b):
    print(val1, val2)   #1  a
                        #2  b
                        #3  c


#48 Think lazy! Use a generator
events = [('learn', 5), ('learn', 10), ('relaxed', 20)]
study_times = (event[1] for event in events if event[0] == 'learn')
minutes_studied = sum(study_times)
print(minutes_studied)  #15


#49 Use itertools
from itertools import islice
lines = ['line1', 'line2', 'line3', 'line4', 'line5', 'line6', 'line7', 'line8',]
first_five_lines = islice(lines, 5)
first_five_lines_2 = islice(lines, 1, 5)
for line in first_five_lines:
    print(line) #line1
                #line2
                #line3
                #line4
                #line5

for line in first_five_lines_2:
    print(line)
                #line2
                #line3
                #line4
                #line5

data = 'ABCDEF'
from itertools import pairwise
for pair in pairwise(data):
    print(pair[0], pair[1]) #A B
                            #B C
                            #C D
                            #D E
                            #E F
                            #F G

from itertools import takewhile
items = takewhile(lambda x:x >= 0, [1, 2, 4, -1, 4, 1])
for item in items:
    print(item) #1
                #2
                #4

