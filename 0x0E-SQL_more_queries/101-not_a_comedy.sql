--  script that lists all shows without the genre Comedy
SELECT DISTINCT s.title
FROM tv_shows s 
LEFT OUTER JOIN tv_show_genres sg 
ON s.id = sg.show_id 
LEFT OUTER jOIN tv_genres g 
ON sg.genre_id = g.id 
WHERE s.id NOT IN (
	SELECT s.id 
	FROM tv_shows s 
	INNER JOIN tv_show_genres sg 
	ON s.id = sg.show_id 
	INNER JOIN tv_genres g 
	ON sg.genre_id = g.id 
	where g.name = 'Comedy') 
ORDER BY s.title ASC;
