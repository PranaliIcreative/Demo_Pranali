#Write a program to print the below pattern

for i in range (6):
    for j in range (6):
        if i+j>5:
            print(" * ",end="")
        else:
            print("  ",end=" ")

    print("")