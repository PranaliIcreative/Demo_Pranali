# By using list comprehension, please write a program to print the list after removing the
# value 24 in [12,24,35,24,88,120,155],

lists=[12,24,35,24,88,120,155]
lists= [x for (i,x) in enumerate(lists) if x is not 24 ]

print(lists)