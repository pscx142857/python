# 当循环执行完成后,执行else里面的语句
# else一般配合break使用,如果执行了break,那么else里面的将不再执行
i = 1
while i < 10:
    if i == 5:
        break
    print(f"这是第{i}次循环")
    i += 1
# 当i等于5时,执行break,结束循环,else里面的语句不再执行
else:
    print("循环已经结束,没有break")