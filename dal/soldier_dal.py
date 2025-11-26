from typing import Optional
from sqlmodel import Session, select, col
from dal.engine import engine
from models.info_soldiers import Soldier


def soldiers_by_distance():
    with Session(engine) as session:
        statement = select(Soldier).order_by("Soldier.his_distance DESC")
        outcome = session.exec(statement)
        return outcome.all