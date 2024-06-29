# select
#     x,
#     y,
#     z,
#     case
#         when x + y > z and
#              x + z > y and
#              y + z > x then 'Yes'
#         else 'No'
#     end as triangle
# from Triangle

# -- SELECT *, IF(x+y>z and y+z>x and z+x>y, "Yes", "No") as triangle FROM Triangle
