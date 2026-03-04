#!/usr/bin/python3
"""
This script connects to a MySQL database and prints all rows from
the 'states' table ordered by id.
"""
import MySQLdb
from sys import argv

db = MySQLdb.connect(host='localhost',
                     port=3306,
                     user=argv[1],
                     passwd=argv[2],
                     db=argv[3])
cur = db.cursor()
cur.execute('''
SELECT * FROM states
WHERE name = %s
ORDER BY id ASC''', (argv[4],))
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db.close()
