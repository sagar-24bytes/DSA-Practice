SELECT t1.id
FROM Weather as t1
JOIN Weather as t2
ON DATEDIFF(t1.recordDate,t2.recordDate)=1 and t1.temperature>t2.temperature;