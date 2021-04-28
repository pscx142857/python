# 遍历key
dic = {"name": "张飞", "age": 10, "height": 300}
print(dic.get("aaa", "键不存在"))
for key in dic:
    print(key)
# 遍历value
for value in dic.values():
    print(value)
# 遍历键值对
for item in dic.items():
    print(item)

for k, v in dic.items():
    print("键:" , k)
    print("值:" ,v)
