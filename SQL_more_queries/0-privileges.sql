-- Privileges
CREATE USER 'user_0d_1'@'localhost';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

CREATE USER 'user_0d_2'@'localhost';

CREATE DATABASE IF NOT EXISTS user_2_db;

GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- List privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
