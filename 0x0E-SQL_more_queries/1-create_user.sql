-- Script that creates the mysql server user user_od_1
-- Should have all privileleges on your Mysql server
-- Password should be set
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.*
TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
