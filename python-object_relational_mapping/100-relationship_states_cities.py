#!/usr/bin/python3
"""
Script that creates the State
"California" with the City "San Francisco"
from the database hbtn_0e_100_usa
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

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State and City objects
    new_state = State(name="California")
    new_city = City(name="San Francisco")

    # Add city to state's cities relationship
    new_state.cities.append(new_city)

    # Add state to session and commit
    session.add(new_state)
    session.commit()

    # Close session
    session.close()
