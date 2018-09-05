# Write your MySQL query statement below
select d.Name as Department, e.name as Employee, e.Salary
from Employee e
inner join Department d on e.DepartmentId = d.Id
inner join (
    select max(ee.Salary) as maxSalary, ee.DepartmentId
    from Employee ee
    group by ee.DepartmentId
) m on e.Salary = m.maxSalary and e.DepartmentId = m.DepartmentId;
