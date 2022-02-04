
class a:
    def f1(self):
        print("class a method")

class b():
    def f1(self):
        print("class b method")
        super(b, self).f1()

class c(a,b):
    def f1(self):
        print("class c method")
        super(c,self).f1()

obj1=c()
obj1.f1()
