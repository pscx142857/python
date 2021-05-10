"""
配置文件操作模块:configparser
[节]
键 = 值
"""
# 导入configparser模块
import configparser
# 创建对象
cfg = configparser.ConfigParser()
# 以只读的方式打开配置文件
cfg.read("db.ini",encoding="utf8")
# 读取所有的节
print(cfg.sections()) # ['global', 'qq']
# 读取指定节下面的所有的键
print(cfg.options("qq")) # ['username', 'sex']
# 读取指定节下面指定键对应的值
print(cfg.get("qq", "sex")) # 男
# 读取指定节下面的所有的键值对
items = cfg.items("global")
print(items)
# 可以直接转成字典
dic = dict(items)
print(dic)