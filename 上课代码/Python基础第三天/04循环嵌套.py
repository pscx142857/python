i = 1 # 行
while i <= 9:

    if i == 5:
        i += 1
        continue
    if i == 6:
        break

    j = 1 # 列
    while j <= i:
        print(f"{i} * {j} = {i * j} \t", end="  ") # end打印的时候以什么结尾
        j += 1
    i += 1
    print()
else:
    print("完整的99乘法表")