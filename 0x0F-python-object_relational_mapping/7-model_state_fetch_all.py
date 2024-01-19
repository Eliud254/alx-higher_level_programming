#!/usr/bin/python3
"""
This script interacts with a MySQL database using SQLAlchemy.
It imports necessary modules and performs basic database operations.
"""

# Importing necessary modules
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Creating a database engine
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')

    # Creating a session using the sessionmaker method
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating tables specified in models
    Base.metadata.create_all(engine)

    # Querying the database for states and printing the results
    states_list = session.query(State).order_by(State.id).all()
    for state in states_list:
        print(f'{state.id}: {state.name}')

    # Closing the current session once all states are printed
    session.close()
