-- This script creates the 'users' table if it doesn't already exist.
-- The table includes an auto-incrementing primary key, a unique email, and a name.
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
	);