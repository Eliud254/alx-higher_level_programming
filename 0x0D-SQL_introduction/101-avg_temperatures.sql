-- Import in hbtn_0c_o database
-- Script that display the top 3 of cities temp
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
