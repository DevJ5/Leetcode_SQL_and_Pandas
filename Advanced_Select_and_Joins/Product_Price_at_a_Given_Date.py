# select t1.product_id, t1.new_price as price
# from Products as t1
# inner join (select product_id, max(change_date) as date from Products where change_date <='2019-08-16' group by product_id) as t2 on t1.product_id = t2.product_id and t1.change_date = t2.date
# union
# select distinct product_id, 10 as price from Products where product_id not in (select product_id from Products where change_date <= '2019-08-16')
