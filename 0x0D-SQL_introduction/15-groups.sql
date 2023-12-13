-- Script that list the number of records with the same score in the table
-- The result should display the scores
-- The number of records for this scores with the label number
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
