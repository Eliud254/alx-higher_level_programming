-- Script that lists all records of the table 
-- Don't list row without a name value
-- Result should display the score and the name
-- Records should be listed by descending score
-- The database name will be passed as an argument to the mysql command
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
