
def checklist(lists):
    if len(lists) == 0:
        return
    b=lists[:4]
    c=[]
    for i in range (len(b)):
        if b[i] in c:
            return False
        else:
            c.append(b[i])
    checklist(lists[4:])
    return True
num =input("enter the list seprated by coma',': ")
lists=num.split(",")
value=checklist(lists)
print(value)