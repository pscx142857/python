# 定义一个99乘法表的函数
def cf99():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f"{j} * {i} = {i*j}\t",end="")
        print()
#调用函数
cf99()