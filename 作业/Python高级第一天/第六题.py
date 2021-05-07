"""
6.从列表中 [“123456”,”456321”,”65721231”,”156746”,”156451455”] 随机
    获取3个元素,将3个数据通过 md5加密后存放到 新的列表里面,可以使用列表推导式
"""
# 导入随机模块
import random
# 导入hashlib模块
import hashlib
# 定义一个列表
ls = ["123456","456321","65721231","156746","156451455"]
# 定义一个空列表
ls2 = []
# 随机获取3个元素
ls_new = random.sample(ls,3)
# print(ls_new)
# 将获取的3个随机元素通过md5加密
for i in ls_new:
    b = i.encode("utf8") # 变量.encode(编码方式)  得到二进制的数据
    # 实例化算法对象
    h = hashlib.md5(b)
    # 获取加密后的结果
    res = h.hexdigest()
    # print(res)
    ls2.append(res)
print(ls2)
# 列表推导式的方式
ls3 = [hashlib.md5(i.encode("utf8")).hexdigest() for i in random.sample(ls,3)]
print(ls3)
