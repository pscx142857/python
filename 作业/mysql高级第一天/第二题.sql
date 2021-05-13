-- A.查询商品数据表中商品名称为”智能相机”的库存数量
select goods_name,goods_number
from ecs_goods
where goods_name = "智能相机";
-- B.查询商品数据表中商品名称为”智能相机”的图片链接地址
select goods_name,goods_img
from ecs_goods
where goods_name = "智能相机";
-- C.查询所有上架的商品名称,is_on_sale 1上架
select distinct goods_name
from ecs_goods
where is_on_sale = 1;
-- D.查询所有未审核的商品名称,is_check 0未审核
select goods_name
from ecs_goods
where is_check = 0;
-- E.查询商品数据表中所有为精品的商品名称,is_best 1精品
select goods_name
from ecs_goods
where is_best = 1;
-- F.查询卖的最贵的商品的名称
select goods_name,max(shop_price)
from ecs_goods;
-- G.查询商品品牌为”仓品”的 所有商品名称和商品价格
select eg.goods_name,eg.shop_price
from ecs_brand join ecs_goods eg on ecs_brand.brand_id = eg.brand_id
where brand_name = "仓品";
-- H.查询商品品牌为”仓品”的 所有商品名称和商品价格 按照价格降序排列
select eg.goods_name,eg.shop_price
from ecs_brand join ecs_goods eg on ecs_brand.brand_id = eg.brand_id
where brand_name = "仓品"
group by shop_price desc;
-- I.查询每个商品品牌的商品数量
select eb.brand_id,count(*)
from ecs_goods join ecs_brand eb on ecs_goods.brand_id = eb.brand_id
group by brand_id;
-- J.查询商品品牌对应的商品数量大于5的商品品牌名称
select eb.brand_id,eb.brand_name,count(*)
from ecs_goods join ecs_brand eb on ecs_goods.brand_id = eb.brand_id
group by brand_id
having count(*) > 5;