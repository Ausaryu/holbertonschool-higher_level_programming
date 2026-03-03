-- A sql script that get
-- all cities from california
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states on state_id = states.id
ORDER BY cities.id ASC;