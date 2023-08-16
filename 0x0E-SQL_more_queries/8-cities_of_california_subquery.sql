-- joins two table without join keyword
SELECT c.id, c.name
FROM cities c, states s
WHERE c.state_id = s.id
AND s.name = 'California'
ORDER BY c.id
ASC;

