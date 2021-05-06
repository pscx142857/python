a = int(input('请输入数字 a：'))
count = int(input('请输入几个数相加：'))

res = 0  # 最终求解的计数器
for i in range(1, count + 1):  # 循环次数 == 相加的数的个数
    # print(i)   # 1,2,3,4
    t = 0  # t 的计数器
    for j in range(0, i):
        # print("*", j)
        t = t + 10 ** j  # 先计算 10**0 + 10**1 + ... + 10**j
        # print("**", t)
    res = res + (a * t)  # 再计算 a * t
print(res)

a = int(input('请输入数字：'))
b = a + a * 11 + a * 111 + a * 1111
print(b)