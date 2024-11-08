# select t1.product_id, t2.first_year, t1.quantity,t1.price
# from Sales as t1
# inner join (select product_id, min(year) as first_year
# from Sales
# group by product_id) as t2
# on t1.product_id = t2.product_id and t1.year = t2.first_year
