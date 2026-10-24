# Write your MySQL query statement below
SELECT e.name
FROM Employee as e
JOIN Employee as e2
ON e.id = e2.managerId
GROUP BY e.id,e.name
HAVING COUNT(e.id)>=5;