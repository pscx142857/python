i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
# 如果break执行了,那么else中的语句将不再执行
else:
    print("循环结束")
