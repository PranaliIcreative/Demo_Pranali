#Write a program which are divisible by 7 and between a given range 0 and n.

def divisibility(Range):
    for i in range(0, Range):
        if i % 7 == 0:
            print(i," ",end=" ")
Range=int(input("enter the end limit of range whose divisibility needed to be tested : "))
divisibility(Range)