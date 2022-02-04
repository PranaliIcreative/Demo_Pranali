# Please write a program to print the list after removing delete even numbers in
# [5,6,77,45,22,12,24].
List =[1,2,3,4,5,6,7,8,9,12,10,45,36]
for i in range (len(List)-1,0,-1):
    if (List[i]%2) == 0:
        List.remove(List[i])
        i+=1

print(List)