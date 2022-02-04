#Write a program which can compute the factorial of a given numbers.The results should
# be printed in a comma-separated sequence on a single line.
import math
def factorial(numbers):
        return 1 if (numbers==1 or numbers==0) else numbers*factorial(numbers-1)
Factorial=[]
numberlist = []

LengthofList=int(input("enter the count of numbers whoes factorial you need : "))
for i in range(LengthofList):
    numb=int(input("enter the number {}".format(i+1)))
    numberlist.append(numb)
    Factorial.append(factorial(numb))
print(",".join(map(str, numberlist)))
print(",".join(map(str, Factorial)))
