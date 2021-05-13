"""

"""
# 列表推导式生成器
# it = (i for i in range(1,1000000000))
# while True:
#     try:
#         print(next(it))
#     except Exception as e:
#         print(e)
#

# 函数生成器,得到1-正无穷的数
def info():
    i = 1
    while True:
        yield i
        i += 1
# 调用一次得到生成器对象
it = info()

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))