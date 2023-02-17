-- Script queries cities from California
-- Uses nested Select statements
SELECT name FROM cities WHERE state_id = (SELECT id FROM states
WHERE name = "California") ORDER BY cities.id ASC;
