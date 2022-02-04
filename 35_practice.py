# a=8
# print(type(range(9,15)))

# a=[2,5,7,9,4,6,15,3,1,8,]
# num=sorted(a,key= list(filter(lambda x:x%2==0,a)),reverse=True)
# # print(list(map(lambda x: x*3 ,a)))
# print(num)
# print(type(sorted))
stringList = []
def find_str(lists):

    if len(lists)==0:
        return

    if type(lists[0])==list:
        list1=lists[0]

        if type(list1[0]) == str:
            stringList.append(list1[0])

        find_str(list1[1:])

    if type(lists[0])==str:
        stringList.append(lists[0])

    find_str(lists[1:])

string_given=[1,'3',546,[9,'rtr',5,[2,88,'25',99,'243'],'rtrve'],234,'235']
find_str(string_given)
print(stringList)