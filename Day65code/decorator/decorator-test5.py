# 原函数还是原函数吗？

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("我是wapper")
        func(*args, **kwargs)  # *args, **kwargs 表示任意数量和类型的参数
    return wrapper


@my_decorator  # 装饰器
def greet(name, message):
    print(name, message)


def greet2(name, message):
    print(name, message)


# 加装饰器的函数，原信息变了，不再是以前的greet函数，而是被wrapper取代
print(greet.__name__)

print(greet2.__name__)