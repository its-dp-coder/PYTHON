x=99
# def func():
#     global x
#     x=12
# func()    
# print(x)

# def f1():
#     x=88
#     def f2():
#         print(x)
#     f2()    
# f1()    
# closure 
# def f1():
#     x=88
#     def f2():
        #   print(x)
#     return f2
# myResult = f1() 
# myResult()  


def coder(num):
    def actual(x):
        return x ** num
    return actual 
f = coder(2)
g= coder(3)
print(f(3))
print(g(3))