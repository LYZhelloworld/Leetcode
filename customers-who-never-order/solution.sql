# Write your MySQL query statement below
SELECT `Name` AS `Customers`
FROM `Customers`
WHERE NOT EXISTS (
    SELECT *
    FROM `Orders`
    WHERE `Customers`.`Id` = `Orders`.`CustomerId`
);
