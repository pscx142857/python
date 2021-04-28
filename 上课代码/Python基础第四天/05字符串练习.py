# strip 去除
name = "  左边空格,右边等号=="
print(name.strip("=")) #以什么字符去除两边的,不填就是以空格来去除
print(name.lstrip())
print(name.rstrip("=="))
# split 分割
name = "张3.李四.王五"
print(name.split("."))
# upper 大写
name = "tony"
print(name.upper())
# lower 小写
name = "Tony"
print(name.lower())
# startswith 以什么开始
name = "huaqizi.avi"
print(name.startswith("hua"))
# endswith   以什么结束
print(name.endswith(".avi"))
# format     格式化
# join  拼接
ls = ["1","a","c"]
str = "-"
print(str.join(ls))
# replace 替换
str = "aabbccddaaa"
new_str =  str.replace("aa","AA")
print(new_str)
# isdigit 是否纯数字
print(str.isdigit())
