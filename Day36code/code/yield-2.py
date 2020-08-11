# 生成器又称迭代器，生成器迭代一次之后就不能再次迭代，生成器不会将所有值存储在内存中，而是实时的生成这些值。

# 创建生成器的其中一种方式

generator1 = (i * i for i in range(1, 6))

print(type(generator1))
print('-' * 20)

for i in generator1:
    print(i)

print('-' * 20)


# 另一种创建生成器的方式就是使用 yield 关键字


def create_generator():
    for i in range(1, 6):
        yield i * i
# return 会终端for循环， yield会挂起。


generator2 = create_generator()  # 当调用create_generator 函数的时候并没有返回计算结果，而是返回了一个生成器对象。

print(generator2)

# 迭代这个生成器对象才会生成计算结果。
for item in generator2:
    print(item)
