-- script to listt geres id by show
SELECT s.title, sg.id AS genre_id
FROM tv_shows s
INNER JOIN tv_show_genres sg
ON s.id = sg.show_id
INNER JOIN tv_genres g
ON sg.genre_id = g.id
ORDER BY s.title, sg.id
ASC;
