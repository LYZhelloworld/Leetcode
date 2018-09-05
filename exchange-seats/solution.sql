# Write your MySQL query statement below
select s1.id, ifnull(s2.student, s1.student) as student
from seat s1
left join seat s2 on s1.id = if(s1.id % 2 <> 0, s2.id - 1, s2.id + 1)
order by s1.id;
