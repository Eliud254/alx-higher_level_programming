-- Sript that converts hbtn_oc_0 database UTF8
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
