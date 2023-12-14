-- Script that creates the table force_name on your MySql server
-- The database name will be passed as an argument of the mysql command
-- If the table force_name alraedy axists ,your script should not fail
CREATE TABLE IF NOT EXISTS force_name(id INT,
name VARCHAR(256) NOT NULL
);
