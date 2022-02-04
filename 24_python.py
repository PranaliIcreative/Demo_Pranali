# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to
# make a list whose elements are intersection of the above given lists.

lists1=[1,3,6,78,35,55]
lists2=[12,24,35,24,88,120,155,55]
lists3=list(set(lists1).intersection(set(lists2)))
print(lists3)
lists4=[value for value in lists1  if value  in lists2]
print(lists4)