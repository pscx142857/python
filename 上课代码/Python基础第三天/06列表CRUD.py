ls = ["张3","李四"]
print(ls)
# append 末尾增加数据
ls.append("王二")
print(ls)
# insert 根据索引插入
ls.insert(1,666)
print(ls)
# extend 扩展
list = ["我是2",777]
ls.extend("list")
print(ls)
# del 根据索引删除数据
del list[0]
print(list)
# remove 删除第一个出现的指定数据
ls2 = [1,2,3,44,55,44]
ls2.remove(44)
print(ls2)
# pop 弹出列表最后一个值
vlu = ls2.pop()
print(vlu)
print(ls2)
# 弹出指定索引的值
vlu = ls2.pop(1)
print(vlu)
print(ls2)
# clear 清空列表
ls2.clear()
print(ls2)
# 查询指定索引的值
ls3 = ["照照","么么","33","44"]
vlu = ls3[2]
print(vlu)
print(ls3[0])
print(ls3[-1]) # 负数指倒数第几个
# 切片得到一个新的列表,原来的不变
ls4 = [0,1,2,3,4,5,6,7]
new_ls = ls4[0:3:2]
print(ls4)
print(new_ls)
# index查询数据第一次出现时的索引
ls5 = [101,99,88,97,88]
i = ls5.index(88)
print(i)
# len查询列表的长度
l = len(ls5)
print(l)
# count 查询数据出现的次数
count = ls5.count(88)
print(count)
# 修改列表元素
ls5[0] = 0
print(ls5)
# sort 升序排序
ls5.sort()
print(ls5)
# 降序排序
ls5.sort(reverse=True)
print(ls5)
# 列表反转
ls5.reverse()
print(ls5)