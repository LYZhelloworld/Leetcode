CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT DEFAULT N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT (
        SELECT DISTINCT `Salary` FROM `Employee` ORDER BY `Employee`.`Salary` DESC LIMIT 1 OFFSET M
      ) AS `getNthHighestSalary`
  );
END
