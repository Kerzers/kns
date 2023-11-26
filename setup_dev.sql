-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS KNS_dev_db;
CREATE USER IF NOT EXISTS 'KNS_dev'@'localhost' IDENTIFIED BY 'KNS_dev_pwd';
GRANT ALL PRIVILEGES ON `KNS_dev_db`.* TO 'KNS_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'KNS_dev'@'localhost';
GRANT PROCESS ON *.* TO 'KNS_dev'@'localhost';
FLUSH PRIVILEGES;
