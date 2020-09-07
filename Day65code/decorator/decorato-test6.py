# 保证原函数还是原来的函数，原信息不发生改变。

import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("我是wapper")
        func(*args, **kwargs)  # *args, **kwargs 表示任意数量和类型的参数
    return wrapper


@my_decorator  # 装饰器
def greet(name, message):
    print(name, message)


def greet2(name, message):
    print(name, message)


print(greet.__name__)  # 此时原函数greet会保留原函数的原信息。

print(greet2.__name__)