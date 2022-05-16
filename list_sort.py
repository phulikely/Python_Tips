lst = ['Stem', 'constitute', 'Sedge', 'Eflux', 'Whim', 'Intrigue']

lst1 = sorted(lst)
print(lst1)  # ['Eflux', 'Intrigue', 'Sedge', 'Stem', 'Whim', 'constitute']

lst2 = sorted(lst, key=str.lower)
print(lst2)  # ['constitute', 'Eflux', 'Intrigue', 'Sedge', 'Stem', 'Whim']

lst_reverse = sorted(lst, key=str.lower, reverse=True)
print(lst_reverse)  # ['Whim', 'Stem', 'Sedge', 'Intrigue', 'Eflux', 'constitute']
