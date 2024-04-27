#!/usr/bin/python3
"""Displays all cities of states given as an argument."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states ON\
                   cities.state_id = states.id WHERE states.name = %s\
                   ORDER BY cities.id", (argv[4], ))
    rows = cursor.fetchall()

    values = []
    for row in rows:
        value = row[0]
        values.append(value)

    result = ", ".join(values)
    print(result)
    cursor.close()
    db.close()
