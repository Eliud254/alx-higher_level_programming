--Script that list all the cities of California that can be found in the database hbtn_0d_usa.
-- Result mudt be sorted in ascending order by cities
-- No using JOIN keyword
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
);
