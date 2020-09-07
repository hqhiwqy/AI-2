# 装饰器的嵌套
# Python 支持多个装饰器


import functools


def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('我是wrapper1')
        func(*args, **kwargs)
    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('我是wrapper2')
        func(*args, **kwargs)
    return wrapper


def my_decorator3(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('我是wrapper3')
        func(*args, **kwargs)
    return wrapper


@my_decorator1
@my_decorator2
@my_decorator3
def greet(message):
    print(message)


# test = my_decorator1(my_decorator2(my_decorator3(greet)))
# test('hello python')


greet('hello world')