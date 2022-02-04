#Write a program that accepts a sentence and calculate the number of uppercase letters
# and lowercase letters.
def length_count(string):
    upper = lower=0
    for i in string :
        if i.isalpha():
            if i.isupper():
                upper += 1
            else:
                lower += 1
    print("Upper {} \nLower {}".format(upper, lower))
lineinput=input("tell us about yourself : ")
length_count(lineinput)


