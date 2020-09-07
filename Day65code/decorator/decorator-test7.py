# 类装饰器: 主要依赖于函数__call__(),每调用一个类的时候就会执行一次。

class Count:
    def __init__(self, func):
        self.func = func
        self.call_num = 0

    def __call__(self, *args, **kwargs):
        self.call_num += 1
        print('call num is {}'.format(self.call_num))
        return self.func(*args, **kwargs)


@Count
def test():
    print('hello world')


test()

test()