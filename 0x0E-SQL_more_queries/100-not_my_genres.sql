-- script to  list all genres not linked to the show Dexter
SELECT DISTINCT g.name
FROM tv_genres g
LEFT OUTER JOIN tv_show_genres sg
ON g.id = sg.genre_id
LEFT OUTER JOIN tv_shows s
ON sg.show_id = s.id
WHERE s.title != 'Dexter'
AND g.id NOT IN 
(SELECT g.id FROM tv_genres g INNER JOIN tv_show_genres sg ON g.id = sg.genre_id INNER JOIN tv_shows s ON sg.show_id = s.id AND s.title = 'Dexter')
ORDER BY g.name
ASC;
