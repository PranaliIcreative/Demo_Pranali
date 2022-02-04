#By using list comprehension, please write a program generate a 3*5*8 3D array whose
# each element is 0.
# for i in range (0,3):
#     list_array.append([])
#     for j in range(0,5):
#         list_array[i].append([])
#         for k in range (0,3):
#             list_array[i][j].append(0)
#
#
array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]

array1 = [[ [0 for col in range(8)] for i in range(5)] for row in range(3)]
print(array)
print(array1)