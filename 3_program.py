#With a given integral number n, write a program to generate a dictionary that contains
# (i,i*i) such that is an integral number between 1 and n (both included). and then the program
# should print the dictionary
import math
DictionaryLength =int(input("enter the length of the dictionary(i,i*i) to be generated : "))
listsrange=range(1,DictionaryLength+1)
Dictonary=dict(zip(listsrange,map(lambda x:x**2,listsrange)))
# for i in range(1,DictionaryLength+1):
#     Dictonary[i]=int(math.pow(i,2))

print (Dictonary)