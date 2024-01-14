#!/usr/bin/python3
""" script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa following 3 arguments ,mysql username,
    mysql password and database name"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    cur.execute('SELECT *FROM states\
               WHERE name LIKE BINARY "N%"\
               ORDER BY states.id ASC;')
    allStates = cur.fetchall()

    for state in allStates:
        print(state)

    cur.close()
    db.close()
