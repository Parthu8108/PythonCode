x = lambda a:a+10
print(x(3))


y = lambda a,b : a+b+4
print(y(10,12))


def func(n):
    return lambda a:a*n
x=func(5)
print(x(2))


def abc(n):
    return lambda a:a*n
x=abc(2)
y=abc(3)
print(x(11))
print(y(11))
