-- script that lists all genres of the show Dexter
SELECT g.name 
FROM tv_genres g
INNER JOIN tv_show_genres sg
ON g.id = sg.genre_id
INNER JOIN tv_shows s
ON sg.show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY g.name
ASC;
