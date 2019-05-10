class A:
    def __init__(self):
        self.a="A"
        print(self.a)


class B:
    def __init__(self):
        self.b="B"
        print(self.b)


class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("hello")

    def funct(self):
        print("Inside the derived class:")
        print(self.a)
        print(self.b)

x=C()
x.funct()
