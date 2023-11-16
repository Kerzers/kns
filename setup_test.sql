-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS KNS_test_db;
CREATE USER IF NOT EXISTS 'KNS_test'@'localhost' IDENTIFIED BY 'KNS_test_pwd';
GRANT ALL PRIVILEGES ON `KNS_test_db`.* TO 'KNS_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'KNS_test'@'localhost';
FLUSH PRIVILEGES;