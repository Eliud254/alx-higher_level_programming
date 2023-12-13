-- Import in hbtn_0c_0 database
-- Script that display the top 3 of the cities temp,during julyand august
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
