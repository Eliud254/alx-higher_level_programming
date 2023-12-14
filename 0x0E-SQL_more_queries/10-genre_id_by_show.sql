-- Import the database dump from hbtn_0d_tvshows to your MySQL server
-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
- List all shows in 'hbtn_0d_tvshows' that have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
