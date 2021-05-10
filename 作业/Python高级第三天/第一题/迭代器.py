"""
for循环底层就是用的迭代器iter实现的
  先创建一个迭代器对象
        iter(容器)
        next(迭代器对象),执行一次就去下一个元素
"""
# 定义一个列表
ls = [1,2,3,4,5,7]
# 创建迭代器对象
it = iter(ls)
# next()执行一次就取下一个数据
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
