# select round(avg(if(order_date = customer_pref_delivery_date,1,0)) * 100,2) as immediate_percentage
# from Delivery d
# where (customer_id, order_date) in
# (
#     select customer_id, min(order_date) as first_order_date
#     from Delivery
#     group by customer_id
# )
