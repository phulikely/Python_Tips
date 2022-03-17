"""
join is a way to concatenate strings together
"""
x = ['7', 'Python', 'Tricks', 'to', 'make', 'your', 'code', 'BETTER', 'and', 'SMARTER']

title_using_join = ('--'*2).join(x)
print(title_using_join)

number_0_after_comma = '{0:.5f} {1} Tricks to make your code better and {2}'.format(7, 'Python', 'smarter')
print(number_0_after_comma)
