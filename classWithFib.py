class demo:
    def __init__(self,no):
        self.no=no

    def fib(self,n):
        a=0
        b=1
        print(a)
        print(b)
        self.n=n
        while n != 0:
            c = a+b
            print(c)
            a=b
            b=c
            c=a
            n-=1

p=demo(10)
p.fib(10)
