# X为形式参数,写在定义的函数括号中,表示占位
def cf(X):
    # Y = X+1
    for i in range(1,X+1):
        for j in range(1,i+1):
            print(f"{j} * {i} = {i*j}\t",end="")
        print()
#调用函数
# 10为实际参数,写在调用的函数括号中,用于参与计算
cf(10)