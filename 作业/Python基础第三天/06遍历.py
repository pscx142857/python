# 用while循环遍历列表
ls = ["张3","李四"]
i = 0
while i < len(ls):
    print(ls[i])
    i += 1
# 用for循环遍历列表
for i in ls:
    print(i)
# 嵌套循环遍历
ls2 = [[0,1],[2,3]]
for i in ls2:
    for j in i:
        print(j)