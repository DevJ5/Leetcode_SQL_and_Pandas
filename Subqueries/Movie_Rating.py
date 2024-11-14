# # Write your MySQL query statement below
# (select name as results
# from Users t1
# inner join (
#     select user_id, count(*) as nr_of_ratings
#     from MovieRating
#     group by user_id
# ) t2 on t1.user_id = t2.user_id
# order by nr_of_ratings desc, name asc
# limit 1)

# union all

# (select title as results
# from Movies t1
# inner join (
#     select movie_id, avg(rating) as avg_rating
#     from MovieRating
#     where created_at like '2020-02-%'
#     group by movie_id
# ) t2 on t1.movie_id = t2.movie_id
# order by avg_rating desc, title asc
# limit 1)
