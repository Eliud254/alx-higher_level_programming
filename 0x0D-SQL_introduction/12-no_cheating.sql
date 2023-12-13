-- Script that updates the score of bob to 10
-- You are not allowed to use bob's id only the name field
-- The database name will be passed as an argument of the mysql command
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
