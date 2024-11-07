# select round(count(distinct(t2.player_id))/count(distinct(t1.player_id)),2) as fraction
# from Activity t1
# left join
# (select player_id, min(event_date) as first_login from Activity  group by player_id) as t2
# on t1.player_id = t2.player_id and t2.first_login = date_sub(t1.event_date, interval 1 day)

