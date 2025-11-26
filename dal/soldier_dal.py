from sqlmodel import Session, select
from dal.engine import engine
from models.info_soldiers import Soldier


def soldiers_by_distance():
    with Session(engine) as session:
        statement = select(Soldier).order_by("Soldier.his_distance DESC")
        outcome = session.exec(statement).all
        return outcome
    
def soldier_by_id_number(id_num:int):
    with Session(engine) as session:
        statement = select(Soldier).where(Soldier.id_number == id_num)
        outcome = session.exec(statement).all
        return outcome
    
        