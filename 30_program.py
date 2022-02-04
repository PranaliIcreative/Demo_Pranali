# Write a program to generate below Pattern:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *

for i in range (6):
    for j in range (6):
        if i>=j:
            print(" * ",end="")

    print("")