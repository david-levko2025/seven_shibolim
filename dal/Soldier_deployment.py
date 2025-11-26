from typing import Optional
from sqlmodel import Session, select, col
from database.db import engine
from models.info_soldiers import Soldier


def read_distance(distance:int):
    with session(engine) as session:
        statement = select(Soldier).sort(Soldier.distance)
        soldiers = session.exec(statement).all()
