# Write your MySQL query statement below
select m.Day, round(cast(m.cancelled as decimal(3, 2)) / cast(m.completed as decimal(3, 2)), 2) as `Cancellation Rate`
from (
    select t1.Request_at as Day, t1.completed, ifnull(t2.cancelled, 0) as cancelled
    from (
        select Request_at, count(*) as completed
        from Trips
        where Trips.Client_Id not in (
            select Users_Id
            from Users
            where Banned <> 'No'
        ) and Trips.Driver_Id not in (
            select Users_Id
            from Users
            where Banned <> 'No'
        )
        group by Request_at
    ) t1 left join (
        select Request_at, count(*) as cancelled
        from Trips
        where Trips.Client_Id not in (
            select Users_Id
            from Users
            where Banned <> 'No'
        ) and Trips.Driver_Id not in (
            select Users_Id
            from Users
            where Banned <> 'No'
        ) and status <> 'completed'
        group by Request_at
    ) t2 on t1.Request_at = t2.Request_at
    order by Day
) m
where (date(m.Day) between '2013-10-1' and '2013-10-3');
