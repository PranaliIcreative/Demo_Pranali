#Use a list comprehension to square each odd number in a list. The list is input by a
# sequence of comma-separated numbers.

charOfNum=input("enter the numbers seprated by coma ',' :").split(',')



charOfNum=[int(value)**2 for value in charOfNum if int(value)%2!=0]
print(",".join(map(str, charOfNum)))
