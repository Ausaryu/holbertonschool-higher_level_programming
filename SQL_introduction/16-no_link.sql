SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND NOT name = ''
ORDER BY score DESC;