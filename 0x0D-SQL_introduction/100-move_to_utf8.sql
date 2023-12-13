-- Sript that converts hbtn_oc_0 database UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
