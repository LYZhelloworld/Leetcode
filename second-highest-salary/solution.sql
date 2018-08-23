# Write your MySQL query statement below
SELECT (
    SELECT DISTINCT `Salary` FROM `Employee` ORDER BY `Employee`.`Salary` DESC LIMIT 1 OFFSET 1
) AS `SecondHighestSalary`;
