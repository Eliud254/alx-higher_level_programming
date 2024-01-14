#!/usr/bin/python3
"""
script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute('SELECT cities.id, cities.name, states.name\
                FROM states\
                INNER JOIN cities ON states.id = cities.state_id\
                ORDER BY cities.id ASC;')
    cities = cur.fetchall()

    for x in cities:
        print(x)

    cur.close()
    db.close()
