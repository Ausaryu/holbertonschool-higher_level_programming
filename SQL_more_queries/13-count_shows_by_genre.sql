-- A sql script that display all show
-- and display null if no genre linked.
SELECT tv_genres.name AS 'genre', count(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres
JOIN tv_show_genres on tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY count(tv_show_genres.genre_id) DESC;