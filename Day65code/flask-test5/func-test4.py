# 闭包：函数的返回值也可以是另外一个函数的对象

def func():
    def get_message(message):
        print(message)
    return get_message


send_message = func()  # 调用

send_message('hello world')