#!/usr/bin/python3
"""
This script connects to a MySQL database and prints all rows from
the 'states' table ordered by id.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                        port=3306,
                        user=argv[1],
                        passwd=argv[2],
                        db=argv[3])
    cur = db.cursor()
    cur.execute('''
    SELECT cities.name FROM cities
    JOIN states ON states.id = cities.state_id
    WHERE %s = states.name
    ORDER BY cities.id ASC''', (argv[4],))
    query_rows = cur.fetchall()
    cities = []
    for row in query_rows:
        cities.append(row[0])

    print(", ".join(cities))
    cur.close()
    db.close()
