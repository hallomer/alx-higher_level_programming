#!/usr/bin/python3
"""Lists all states with a name starting with Nfrom hbtn_0e_0_usa db."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE\
                   BINARY 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
