# You are required to write a program to sort the (name, age, height) tuples by ascending
# order where name is string, age and height are numbers. The tuples are input by console.
# The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.

def Enter_values():
    name=input(" name")
    age=(input(" age"))
    score=(input(" score"))
    return (name, age, score)
def Sort(List=[]):
    # n = len(List)
    # print(n)
    #
    # for i in range(n):
    #     for j in range(n - i - 1):
    #         print(List[j][0])
    #         if List[j][i] > List[j + 1][i]:
    #             List[j], List[j + 1] = List[j + 1], List[j]
    #
    # return List
    return sorted(List)



candidateList =[]
data_requires=int(input("enter the number of candidates data you require : "))
for i in range(data_requires):
    candidateList.append(Enter_values())

print(Sort(candidateList))


print(candidateList)