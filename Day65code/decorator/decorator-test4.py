# 带有多个参数的装饰器
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("我是wapper")
        func(*args, **kwargs)  # *args, **kwargs 表示任意数量和类型的参数
    return wrapper


@my_decorator  # 装饰器
def greet(name, message):
    print(name, message)


greet('hello', 'python')