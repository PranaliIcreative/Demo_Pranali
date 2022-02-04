#using super in multiple inheritance.

class a:
    def __init__(self):
        print("class a method")


class b:
    def __init__(self):
        print("class b method")
        super(b,self).__init__()



class c(b,a):
    def __init__(self):
        print("class c method")
        super(c,self).__init__()

obj1=c()
# obj1.f1()
# obj1()