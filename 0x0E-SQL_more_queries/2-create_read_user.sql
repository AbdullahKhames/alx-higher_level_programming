-- create user and database all together
CREATE DATABASE IF NOT EXISTS hbtn_0d_2 CHARACTER SET =  utf8mb4 COLLATE = utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
