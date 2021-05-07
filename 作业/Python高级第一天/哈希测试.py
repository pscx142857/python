import random
import hashlib
by = []
li = ["123456", "456321", "65721231", "156746", "156451455"]
# 取出3个随机的元素
res = random.sample(li, 3)
print(res)
# 将元素转换成字符串 再转换成二进制文件
str = ", ".join(res)
print(str)
info = str.encode("utf8")
print(info)
# 导入模块 将数据通过md5进行加密
h = hashlib.md5(info)
bn = h.hexdigest()
by.append(bn)
print(by)