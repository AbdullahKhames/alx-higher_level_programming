-- script to listt geres id by show
USE hbtn_0d_tvshows;
SELECT s.title, g.id
FROM tv_shows s
INNER JOIN tv_show_genres sg
ON s.id = sg.show_id
INNER JOIN tv_genres g
ON sg.genre_id = g.id
ORDER BY s.title, g.id
ASC;
