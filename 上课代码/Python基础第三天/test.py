i = 1
p = 1
sum = 0
while p <= 9:
    while i <= p:
        sum = i * p
        print(f"{i} * " f"{p} = " f"{sum}",end="   ")
        i += 1
    print()
    p += 1
    i = 1


