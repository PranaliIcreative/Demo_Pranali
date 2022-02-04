# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list
# after removing all duplicate values with original order reserved

def duplicate(list1):
    duplicate = []
    unique = []
    for i in list1:
        if i not in duplicate:
            duplicate.append(i)
            unique.append(i)
    return unique


list1=[12,24,35,24,88,120,155,88,120,155]
print(duplicate(list1))