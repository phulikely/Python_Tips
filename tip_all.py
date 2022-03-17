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



