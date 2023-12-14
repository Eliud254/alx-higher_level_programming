-- Script that list all the cities of califonia that can be found in the database
-- The state table contains only one record where name =califonia
-- Results must be sorted in asending order by cities
-- You are noy allowed to use the join keyword
-- The database name will be passed as an argument of the mysql command
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
);
