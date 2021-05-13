/*
 4.编写sql语句获取最新发布数据
 */
select *
from news
order by date desc
limit 1;