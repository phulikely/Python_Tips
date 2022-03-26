#28 Use any instead of loop
numbers = [-1, -2, -4, 0, 3, -7]
has_positives = any(n > 0 for n in numbers)
print(has_positives) #True


#29 Replace if statement with if expression
x = 1 if has_positives else 2
print(x)