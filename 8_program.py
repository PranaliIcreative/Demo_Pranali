#Write a program that computes the net amount of a bank account based a transaction log
# from console input. The transaction log format is shown as following:
Transections=[]
Balance = 0
def diposite():
    Transections.append(int(input("enter the value to be deposited : ")))
def withdraw():
    Transections.append(-int(input("enter the value to be withdrawn : ")))
def compute():

    for i in Transections:
        global Balance
        Balance+=i


print("welcome")
key=1
while key==1:
    action=input('''Select your action
            1. Diposite(d)
            2.Withdraw(w)
            3.Exit(e)''')
    if action=='d' or action=='D':
        diposite()
    if action == 'w' or action == 'W':
        withdraw()
    if action == 'e' or action == 'E':
        compute()
        print("Balance : ",Balance)
        key=0
