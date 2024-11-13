# select if(id = (select count(*) from Seat), if(id % 2 = 0, id-1, id) ,if(id % 2 = 0, id-1, id+1)) as id, student
# from seat
# order by id asc
