# 5.开发敏感词语过滤程序，提示用户输入内容，如果用户输入的内容中包含特殊的字符： 如 "手枪" 等，将内容替换为 *
print("本系统敏感词语包含\"飞机\"\"大炮\"\"坦克\"")
# 提示用户输入想说的话
str = input("请输入你想说的话:")
# 根据需求替换掉敏感词汇
str = str.replace("飞机","*").replace("大炮","*").replace("坦克","*")
# str = str.replace("大炮","*")
# str = str.replace("坦克","*")
# 输出处理后用户说的话
print(str)