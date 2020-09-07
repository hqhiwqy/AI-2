# 函数里定义函数

def func(message):
    def get_message(message):
        print(message)
    return get_message(message)


func('hello world')