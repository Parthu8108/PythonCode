class A:
    def __init__(self,no):
        self.no=no

    def funct(self):
        print(self.no)

class B(A):
    pass

x = B(10)
x.funct()  
