i = 1
while i <= 10000 :
    if i == 360:
        i += 1 # 预防进入死循环
        continue # 不执行本次循环,后面的继续
    if i == 366:
        break # 之后的循环都不再执行,直接结束
    print(f"我爱你,第{i}遍")
    i += 1