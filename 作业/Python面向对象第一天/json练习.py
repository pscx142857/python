import simplejson
# 打开文件
fp = open("data.txt", "r", encoding="utf8")
# 操作文件
data = fp.read()
# print(data)
cards = data.split("\n")
# print(cards)
# 关闭文件
fp.close()
# print(cards)
for card in cards:
    dic = simplejson.loads(card)
    print(type(dic))