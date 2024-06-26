# -- select if(count(num) = 1, num, null) as num
# -- from MyNumbers
# -- group by num
# -- order by
# --     count(num) asc,
# --     num desc
# -- limit 1

# select max(num) as num from (select num from MyNumbers group by num having count(num) = 1) sub

# -- SELECT MAX(num) AS num  FROM MyNumbers WHERE num IN (SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(*) = 1);
# -- SELECT (SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(num) = 1 ORDER BY num DESC LIMIT 1) AS num;
