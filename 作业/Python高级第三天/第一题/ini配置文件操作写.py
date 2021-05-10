# 导入configparser
import configparser
# 创建对象
cfg = configparser.ConfigParser()
# 打开文件
cfg.read("db.ini",encoding="utf8")
# 修改指定节下面指定键的值,没有就增加
cfg.set("qq","sex","女")
# 写入文件
cfg.write(open("db.ini","w",encoding="utf8"))
# 增加节
cfg.add_section("love")
# 写入文件
cfg.write(open("db.ini","w",encoding="utf8"))
# 删除节
cfg.remove_section("love")
# 写入文件
cfg.write(open("db.ini","w",encoding="utf8"))
# 删除指定节下面的键值对
cfg.remove_option("qq","name")
# 写入文件
cfg.write(open("db.ini","w",encoding="utf8"))