-- script to get number of shows by genre
SELECT g.name AS genre, COUNT(sg.genre_id) AS number_of_shows
FROM tv_genres g
LEFT OUTER JOIN tv_show_genres sg
ON g.id = sg.genre_id
WHERE sg.show_id IS NOT NULL
GROUP BY sg.genre_id
ORDER BY number_of_shows
DESC;
