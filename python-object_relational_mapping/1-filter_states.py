#!/usr/bin/python3
"""
Lists all states starting with
'N' from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # Connect to MySQL
    db_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=passwd,
        db=db
    )
    cursor = db_connect.cursor()

    # Case-sensitive match using BINARY
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    )                                                                    
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db_connect.close()
