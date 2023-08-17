-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT g.name , SUM(r.rate) AS rating
FROM tv_genres g
INNER JOIN tv_show_genres sg
ON g.id = sg.genre_id
INNER JOIN tv_shows s
ON s.id = sg.show_id
INNER JOIN tv_show_ratings r
ON s.id = r.show_id
GROUP BY g.name
ORDER BY SUM(r.rate) DESC,
g.name ASC;
