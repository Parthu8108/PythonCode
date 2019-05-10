class A:
    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name

class B(A):
    def __init__(self,name,add):
        A.__init__(self,name)
        self.add=add

    def getAdd(self):
        return self.add

class C(B):
    def __init__(self,name,add,no):
        B.__init__(self,name,add)
        self.no=no

    def getNo(self):
        return self.no

object=C("Parth","Noida",100)
p=object.getNo()
q=object.getName()
r=object.getAdd()
print(p)
print(q)
print(r)
