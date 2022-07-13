def do_one(a):
    print('one: a*2 = ', a*2)

def do_two(b):
    print('two: b*2 = ', b*3)

def do_three(c):
    print('three: c*3 = ', c*3)

def do_default(d):
    print('default: d = ', d)


x = 3

# not good code
if x == 1:
    do_one(x)
elif x == 2:
    do_two(x)
elif x ==3:
    do_three(x)
else:
    do_default(x)

# better code
actions = {1: do_one,
           2: do_two,
           3: do_three,
           4: do_default,
           }
act = actions.get(x, do_default)
act(x)