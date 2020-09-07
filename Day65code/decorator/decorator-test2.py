def my_decorator(func):
    def wrapper():
        print("我是wapper")
        func()

    return wrapper


@my_decorator  # 装饰器
def greet():
    print('hello world')


def greet2():
    print('hello')


greet()
greet2()

# @语法糖

# 结论：装饰器本质上就是一个函数，就是函数的函数。
# 作用： 不改变原函数的功能的基础上，给原函数额外的功能。
