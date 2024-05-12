username = 'nikhil'

def func():
    # username = 'nk'
    print(username)

func()
print(username)


x = 98
# def func2(y):
#     z = x + y
#     return z

# result = func2(2)
# print(result) 


# def func3():
#     global x 
#     x = 20
 
# func3()
# print(x)


# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2

# my_result  = f1()
# my_result()


def nikhilCoder(num):
    def actual(x):
        return x ** num
    return actual




square = nikhilCoder(2)
print(square(3))
cube = nikhilCoder(3)