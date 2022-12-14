def f(x):
    x**2

g = f
# print(f(1))
# print(g(1))

def calc(x):
    return x * 10

def math(op,x):
    print(op(x))

math(calc,10)
# //////////////////////////////////
# def sum(x,y):
#     return x+y
sum = lambda x,y: x+y
def mult(x,y):
    return x*y

def sum(x,y):
    return x+y
def calc(op,x,y):
    print(op(x,y))

calc(mult, 4, 5)
calc(sum, 4, 5)
calc(lambda x,y: x+y, 4, 5)

