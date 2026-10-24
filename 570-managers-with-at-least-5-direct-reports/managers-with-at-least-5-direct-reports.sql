# Write your MySQL query statement below
SELECT e.name
FROM Employee as e
WHERE e.id IN (
    SELECT e2.managerId
    FROM Employee as e2
    WHERE e2.managerId IS NOT NULL
    GROUP BY e2.managerId
    HAVING COUNT(*)>=5    
);