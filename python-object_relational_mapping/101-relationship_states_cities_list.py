#!/usr/bin/python3
"""
Script that lists all State objects and
corresponding City objects
contained in the database hbtn_0e_101_usa
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

    # Query all State objects, ordered by id
    # Using joinedload to fetch cities in the same query
    states = session.query(State).order_by(State.id).all()

    # Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))
        # Display cities for this state, sorted by id
        for city in sorted(state.cities, key=lambda x: x.id):
            print("    {}: {}".format(city.id, city.name))

    # Close session
    session.close()
