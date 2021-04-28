# 写代码，有如下列表，请按要求实现每个功能
#     li = ['ethan', 'zoran', 'jim']
#     a. 计算列表长度并输出
#     b. 列表中追加元素 “lucy”，并输出添加后的列表
#     c. 请在列表的第 1 个位置插入元素 “Tony”，并输出添加后的列表
#     d. 请修改列表第 2 个位置的元素为 “Kelly”，并输出修改后的列表
#     e. 请删除列表中的元素 “ethan”，并输出修改后的列表
#     f. 请删除列表中的第 2 个元素，并输出删除的元素的值和删除元素后的列表
li = ['ethan', 'zoran', 'jim']
# 计算li的长度
print(len(li)) #3
# 追加元素"lucy"
li.append("lucy")
print(li) # ['ethan', 'zoran', 'jim', 'lucy']
# 在列表的第一个位置插入"Tony"
li.insert(0,"Tony")
print(li) # ['Tony', 'ethan', 'zoran', 'jim', 'lucy']
# 修改列表的第二个位置的元素为"Kelly"
li[1] = "Kelly"
print(li) # ['Tony', 'Kelly', 'zoran', 'jim', 'lucy']
# 删除列表中的"ethan"
li = ['ethan', 'zoran', 'jim']
li.remove("ethan")
print(li)
# 删除列表中的第二个元素
del li[1] # li.pop(1)
print(li)