def add(a,b):
    c = a+b
    return c # 必须要有返回值,后面的代码才能使用函数计算的结果

c = add(9,10)
print(c+10)

def max_3(a,b,c):
    ls = [a,b,c]
    return max(ls)

print(max_3(99,55,88))