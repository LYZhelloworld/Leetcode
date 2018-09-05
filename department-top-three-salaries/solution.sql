# Write your MySQL query statement below
select d.Name as Department, e.name as Employee, e.Salary
from Employee e, Department d
where e.DepartmentId = d.Id
and (
    select count(distinct Salary)
    from Employee
    where DepartmentId = d.Id
    and Salary > e.Salary
) < 3;
