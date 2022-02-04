# # # # # #private method test
# # # # #
# # # # # class Base:
# # # # #
# # # # #     # Declaring public method
# # # # #     def fun(self):
# # # # #         print("Public method")
# # # # #
# # # # #     # Declaring private method
# # # # #     def _fun(self):
# # # # #         print("Private method")
# # # # #
# # # # #
# # # # # # Creating a derived class
# # # # # class Derived(Base):
# # # # #     def __init__(self):
# # # # #         # Calling constructor of
# # # # #         # Base class
# # # # #         Base.__init__(self)
# # # # #
# # # # #     def call_public(self):
# # # # #         # Calling public method of base class
# # # # #         print("\nInside derived class")
# # # # #         self.fun()
# # # # #
# # # # #     def call_private(self):
# # # # #         # Calling private method of base class
# # # # #         self.__fun()
# # # # #
# # # # #
# # # # # # Driver code
# # # # # obj1 = Base()
# # # # #
# # # # # # Calling public method
# # # # # obj1.fun()
# # # # #
# # # # # obj2 = Derived()
# # # # # obj2.call_public()
# # # # #
# # # # # obj1._fun()
# # # # # # raise an AttributeError
# # # # #
# # # # # # Uncommenting obj2.call_private()
# # # # # # will also raise an AttributeError
# # # #
# # # # def ReturnTypeCheck(**var):
# # # #     print(var)
# # # # name=['ram','riya','shiv','radha']
# # # # scores=[22,34,99,50]
# # # # ReturnTypeCheck(name)
# # #
# # # #not enough values to unpack (expected 3, got 2)
# # # def errorType(a,b,c):
# # #     return a,b
# # #
# # # x,y,z=errorType(8,9,10)
# # # print(x,y,z)
# #
# # #too many values to unpack (expected 3)
# #
# # def errorType(a,b,c):
# #     return a,b,c,12
# #
# # x,y,z=errorType(8,9,10)
# # print(x,y,z)
#
#
# import datetime
# print(datetime)
# #output : <module 'datetime' from '/usr/lib/python3.6/datetime.py'>

print(super)