# 可迭代对象：使用 for...in 遍历的对象就是可迭代对象，像字典，列表，元组，字符串都是可迭代对象。

list1 = [1, 2, 3, 4]

for item in list1:
    print(item)

print('-'*20)

list2 = [i*i for i in range(1, 6)]  # 列表推导式

for item in list2:
    print(item)
