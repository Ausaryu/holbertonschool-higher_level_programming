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
    SELECT id, name FROM states
    WHERE name LIKE BINARY 'N%'
    ORDER BY id ASC''')
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
