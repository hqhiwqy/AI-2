# 带有一个参数的装饰器
def my_decorator(func):
    def wrapper(message):
        print("我是wapper")
        func(message)
    return wrapper


@my_decorator  # 装饰器
def greet(message):
    print(message)


greet('hello')