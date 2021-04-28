ls = [0,1,2,3,4,5]
# append在列表末尾追加一个数据
ls.append(6)
print(ls)
# insert根据索引插入一个数据
ls.insert(0,9)
print(ls)
# extend拼接两个列表
ls1 = [0,1]
ls2 = [2,3]
ls1.extend(ls2)
print(ls1)
# del 根据索引删除数据
ls3 = [1,2,3,4]
del ls3[0]
print(ls3)
# 根据索引删除数据
ls3.pop(2)
print(ls3)
# remove 删除指定的数据,第一次出现的值
ls4 = [1,22,3,22]
ls4.remove(22)
print(ls4)
# clear 清空列表
ls4.clear()
print(ls4)
# 修改元素的值
ls5 = [0,1,2,3,4]
ls5[0] = 99
print(ls5)
# 根据索引查询元素的值
print(ls5[0])
# 根据值来查询索引
print(ls5.index(99))
# 查询列表的长度
print(len(ls5))
# 查询一个元素在列表中出现的次数
ls6 = [22,33,44,22]
print(ls6.count(22))
# 按升序排序
ls6.sort()
print(ls6)
# 按降序排序
ls6.sort(reverse = True)
print(ls6)
# 列表反转
ls6.reverse()
print(ls6)