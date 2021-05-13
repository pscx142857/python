/*
 事务:是一段连续的,不可分割sql语句,事务内的所有的sql语句,要不集体成功,要不集体失败.如果存在部分成功,
     但是另一部分失败,应该将成功对数据的影响去除(回滚)!

 事务的操作:
    开启事务:   将后续执行的sql语句,在内存中模拟执行,结果生成在内存里面
        begin或者start transaction
    提交事务:   将内存中的结果,一次性写入数据库
        commit
    回滚事务:   将内存中的结果清空
        rollback

 事务适用于哪些语法:并不是所有的语法都受事务的控制
    只要不是修改表格里面的数据,都不会受到事务的影响
    例如:查询语句
        建表语句
        删除表的语句
 事务的特性:
    1.原子性(Atomicity)
        事务是一个不可分割的工作单位,事务中的操作要么都发生,要么都不发生.
    2.一致性(Consistency)
        事务前后数据的完整性必须保持一致
    3.隔离性(Isolation)
        多个用户并发访问数据时,一个用户的事务不能被其他用户的事务所干扰,多个并发事务之间的数据要相互隔离
    4.持久性(Durability)
        一个事务一旦被提交,它对数据库中的数据改变就是永久性的
 */
 # 袁术  给 袁绍 转1000
# 开启事务
start transaction;
# 袁术-1000
update student
set money = money -1000
where stu_name= '袁术';
# 袁绍+1000
update student
set money = money + 1000
where stu_name='袁绍';
# 提交事务
commit;
# 开启事务
begin;
# 执行失败
update student
set money = money - 1000
where stu_name='袁1';
# 袁绍+1000
update student
set money = money +1000
where stu_name='袁绍';
# 回滚
rollback;
