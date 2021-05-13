"""
6.得到”13645450000”-”13645459999”的所有电话号码,将其存放到列表里面
"""
# # 创建一个可以得到13645450000-13645459999的生成器
bl = (i for i in range(13645450000,13645460000))
# 定义一个空列表
ls = []
while True:                 # 死循环,一直取生成器里面的值
    try:                    # 当生成器穷尽时再取值会报StopIteration异常
        s = str(next(bl))   # 可能出现异常的代码
        ls.append(s)
    except StopIteration:
        print("已经穷尽了")  # 有异常时执行的代码
        break               # 生成器穷尽时,会抛出异常,用break结束死循环
# 打印ls列表
print(ls)

# def info():
#     i = 13645450000
#     while True:
#         yield i
#         i += 1
# it = info()
# ls = []
# i = 1
# while i<=10000:
#     s = str(next(it))
#     ls.append(s)
#     i += 1
# print(ls)