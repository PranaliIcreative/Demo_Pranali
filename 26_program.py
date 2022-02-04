# Use a list comprehension to square each odd number in a list. The list is input by a
# sequence of comma-separated numbers.

stringInput=input("enter the list seprated by coma',' : ").split(',')

stringInput=[int(value)**2 for value in stringInput]
print(",".join(map(str, stringInput)))