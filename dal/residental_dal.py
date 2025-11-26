from models.residence import Residence
from dal.engine import engine
from sqlmodel import Session,select


def beds_left(num_residence):
    reaction = {}
    rooms_in_residence = [0,0,0,0,0,0,0,0,0,0]
    with Session(engine) as session:
        statement = select(Residence).where(Residence.residence == 1)
        outcome = session.exec(statement)
        for room in outcome:
            rooms_in_residence[room.room_number] += 1
        for room in range(len(rooms_in_residence)):
            if room == 0:
                reaction["The rooms are full "] += f"{str(room)}" 
            elif 0 < room < 8:
                reaction["there are particial rooms"] += f"{str(room)}" 
            else:
                reaction["The rooms are empty"] += f"{str(room)}"
    return reaction

