# 将函数作为另外一个函数的参数

def get_message(message):
    return message


def send_message(func, message):
    print(func(message))


send_message(get_message, 'hello world')