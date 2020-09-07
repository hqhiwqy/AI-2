def my_decorator(func):
    def wrapper():
        print("我是wapper")
        func()

    return wrapper


def greet():
    print('hello world')


test = my_decorator(greet)  # test 变量指向内部函数 wrapper 调用 greet

test()

# 上述代码：my_decorator()是装饰器
# 作用：把真正需要执行的函数greet()包裹在其中，并且改变了它的行为，但是原函数greet不变。
