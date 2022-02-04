#Write a program which accepts a sequence of comma-separated numbers from the
# console and generate a list and a tuple which contains every number.

Consoleinput=input("enter the numbers seprated by coma ',' : ")
RequiredList=Consoleinput.split(",")
RequiredTuple=tuple(RequiredList)
print(RequiredTuple)
print(RequiredList)