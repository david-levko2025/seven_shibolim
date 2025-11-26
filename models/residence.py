from typing import Optional
from sqlmodel import Field,SQLModel


class Residence(SQLModel,table= True):
    id_number :int   
    residence :int
    room_number :int