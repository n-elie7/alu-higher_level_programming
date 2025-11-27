#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine connection to MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        ),
        pool_pre_ping=True,
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects, ordered by id
    cities = session.query(City).order_by(City.id).all()

    # Display results
    for city in cities:
        print("{}: {} -> {}".format(
            city.id, city.name, city.state.name
        ))

    # Close session
    session.close()
