#!/usr/bin/python3
"""
This script connects to a MySQL database using SQLALchemy.
"""
import sys
from model_state import Base, State
from model_city import Base, City

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    results = session.query(State, City)\
        .join(City, City.state_id == State.id)\
        .order_by(State.id)\
        .all()
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
