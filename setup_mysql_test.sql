-- create if not exit new database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create the new user for database hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- granting priviledges
GRANT ALL PRIVILEGES ON hbnb_test_db. * TO 'hbnb_test'@'localhost';
-- have SELECT privilege on the database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- flush priviledges
FLUSH PRIVILEGES;
