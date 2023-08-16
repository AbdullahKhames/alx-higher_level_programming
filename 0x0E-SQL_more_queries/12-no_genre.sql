-- outer joinn where field is null
SELECT s.title, sg.genre_id
FROM tv_shows s
LEFT OUTER JOIN tv_show_genres sg
ON s.id = sg.show_id
WHERE sg.genre_id IS NULL
ORDER BY s.title, sg.genre_id
ASC;
