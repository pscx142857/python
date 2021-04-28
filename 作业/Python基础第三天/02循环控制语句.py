# break执行后,跳出循环,后面的都不再执行
i = 1
while i < 10:
    # 在第五次的时候结束循环,后面的不再执行
    if i == 5:
        break
    print(f"这是第{i}次循环")
    i += 1
# continue 跳过本次循环,后面的还会执行
j = 1
while j < 10:
    # 跳过第五次循环,后面的循环还会执行
    if j == 5:
        j += 1 # 防止进入死循环
        continue
    print(f"这是第{j}次循环")
    j += 1