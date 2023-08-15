-- script to show top city
SELECT t.city, AVG(value) AS avg_temp
FROM temperatures t
WHERE t.month IN (7, 8)
GROUP BY `city`
ORDER BY avg_temp
DESC
LIMIT 3;
