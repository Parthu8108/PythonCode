def fib():
    a=0
    b=1
    n=input('Enter n\n')
    print('The fib series is:\n')
    print(a)
    print(b)
    while n>0:
        c=a+b
        print(c)
        a=b
        b=c
        c=a
        n-=1
        
fib()        