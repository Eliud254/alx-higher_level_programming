-- Import in hbtn_0c_0 database
-- Script that display the top 3 of the cities temp,during julyand august
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
