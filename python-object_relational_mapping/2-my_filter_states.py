#!/usr/bin/python3
"""Safe script to avoid SQL injection
while filtering states by name"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to database
    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=username, passwd=password, db=db_name
    )

    cursor = conn.cursor()
    # SAFE query using parameterized execution
    query = """SELECT *
    FROM states
    WHERE name = '{}'
    ORDER BY id ASC""".format(state_name)
    cursor.execute(
        query
    )

    # Fetch and print results
    for row in cursor.fetchall():
        print(row)

    # Close connection
    cursor.close()
    conn.close()
