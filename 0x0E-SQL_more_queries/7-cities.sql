-- Creates a table
-- Input rows inside the table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
( id INT AUTO_INCREMENT NOT NULL UNIQUE,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id)
);
