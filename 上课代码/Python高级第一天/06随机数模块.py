"""
random随机数模块
"""
import random
# 随机生成0-1之间的浮点数
print(random.random())
# 随机生成a-b之间的整数
print(random.randint(0, 9))
# 随机从序列中取一个元素
ls = [1,2,3,4,5,7,8,9,10]
print(random.choice(ls))
# 随机从序列中取几个元素
st = "qwertyuioplkjhgfdsazxcvbnm1234567890ZXCVBNMLKJHGFDSAQWERTYUIOP"
ls1 = random.sample(st, 6)
print("".join(ls1))