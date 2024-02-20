-- This is st up for shanfengco DATABASE

CREATE DATABASE IF NOT EXISTS shanfengco_db;
CREATE USER IF NOT EXISTS 'shanfengco'@'localhost' IDENTIFIED BY 'shanfengco_pwd';
GRANT ALL PRIVILEGES ON `shanfengco_db`.* TO 'shanfengco'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'shanfengco'@'localhost';
FLUSH PRIVILEGES;