# 假设有一个列表 names=[“曹操”,”刘备”,”关羽”,”张飞”,”小乔”,”诸葛亮”],如何依次打印出里面所有的人名
names = ["曹操","刘备","关羽","张飞","小乔","诸葛亮"]
# for遍历后打印出来即可
for i in names:
    print(i)
# while 循环遍历打印
j = 0
while j < len(names):
    print(names[j])
    j += 1