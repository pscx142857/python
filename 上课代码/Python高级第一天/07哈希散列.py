"""

"""
# 导入hashlib模块
import hashlib
# 将密码888888通过算法进行加密
password = b"888888"
# print(password)
# 实例化算法对象
h = hashlib.md5(password)
# 获取加密后的数据
res = h.hexdigest()
st = str(res)
print(st)
ls = []
print(ls.append(st))