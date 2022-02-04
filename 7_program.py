#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the
# value of a.

def addition_Function(a):
    b=(a*1000+a*100+a*10+a)
    return b+b//10+b//100+b//1000

number=int(input("enter one digit number(0-9) to be added in the given sequence :"))
print(addition_Function(number))