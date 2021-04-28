# 使用for循环完成99乘法表
# 外层循环控制行
for i in range(1,10):
    # 内层循环控制列
    for j in range(1,i+1):
        print(f"{j} * {i} = {j*i}\t",end=" ")
    print()