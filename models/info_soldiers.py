from typing import Optional
from sqlmodel import Field,SQLModel


class Soldier(SQLModel, table = True):
    id_number : Optional[int] = Field(default= None, primary_key= True)
    f_name : str 
    l_name : str 
    gender : str
    city : str
    distance :int
    status : bool #for now