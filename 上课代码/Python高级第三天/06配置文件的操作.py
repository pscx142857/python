# 导入configparser模块
"""
读取ini文件:
import configparser
# 实例化对象
cfg = configparser.ConfigParser()
# 使用读的方式打开配置文件
cfg.read("db.ini",encoding="utf8")

# 获取所有的节
sections = cfg.sections()
print(sections) # ['database', 'qq']

# 获取指定节(database)下面的所有键
keys = cfg.options("database")
print(keys) # ['host', 'port', 'user', 'password']

# 获取指定节下面指定的键对应的值
value = cfg.get("database","user")
print(value) # root

# 获取指定节下面的所有键值对
items = cfg.items("database")
print(items) # [('host', 'localhost'), ('port', '3309'), ('user', 'root'), ('password', 'root')]
# 针对items这种格式的数据,可以直接转成字典
dic = dict(items)
print(dic)
"""
"""
写入ini文件
"""
# 导入configparser模块
import configparser
# 创建configparser对象
cfg = configparser.ConfigParser()
# 使用读的方式打开配置文件
cfg.read("db.ini",encoding="utf8")

# 修改指定节下面的键对应的值
cfg.set("database","user","pengsheng")
cfg.write(open("db.ini","w"))

# 添加一个节
cfg.add_section("loves")
cfg.write(open("db.ini","w"))

# 删除一个节
cfg.remove_section("qq")
# 删除指定的节中的键值对
cfg.remove_option("database","user")

# 将删除后的内容写入文件
cfg.write(open("db.ini","w"))
