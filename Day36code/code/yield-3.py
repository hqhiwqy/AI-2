# yield 作用

# 1. return 会终止for循环，而 yield 不会

# 2. return 会种植后面的代码，而 yield 不会终止后面的代码， yield 不仅会返回值还会继续执行后面的代码。

def test_yield():
    yield '我是函数的返回值！'
    print('我是return后面的代码。')


generator = test_yield()

for i in generator:
    print(i)


print('-'*20)
# 举例1：创建一个非常大的列表
# generator2 = [i for i in range(100000000000)]

# 举例2：求1-10的偶数

# 简单写法


def test1():
    result = []
    for i in range(1, 11):
        if i % 2 == 0:
            result.append(i)
    return result


res1 = test1()

for i in res1:
    print(i)


print("-"*20)


# 高级写法

def test2():
    for i in range(1, 11):
        if i % 2 == 0:
            yield i


res2 = test2()

for i in res2:
    print(i)