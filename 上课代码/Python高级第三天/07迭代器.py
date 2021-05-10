"""
    for循环的底层实现就是用的迭代器
    先创建一个迭代器对象
        iter(容器)
        next(迭代器对象),执行一次就去下一个元素
"""
ls = [1,2,3,4,5,6,7]
# 创建迭代器对象
i = iter(ls)
# 执行一次,就取下一个元素
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
