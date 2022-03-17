"""
map take a function and a list as parameters, 
it applies the function to every item in the list. 
It is really handy because it avoids using loops, and it is faster.
"""
x = [1, 2, 3, 4, 5]


def cal_square(x):
    return x**2 if x > 4 else x


a = list(map(cal_square, x)) # them list vao vi map tra ve list va de dang doc dc hon
print(a)

wordlist = ['a', 'b', 'c']
newlist = map(str.upper, wordlist)
print(list(newlist))
