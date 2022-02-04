# Please write a program which accepts a string from the console and prints it in reverse
# order.
def reverse(StrInput):
    print("running function....")
    reverseStr=""
    for i in range(len(StrInput)-1,-1,-1):
        reverseStr+=StrInput[i]
    return reverseStr

StringInput=input("enter a string : ")
print(reverse(StringInput))
