from typing import Optional
from sqlmodel import Field,SQLModel

class Residential_base(SQLModel,table= True):
    def base_sorting(soldiers: list[list[str]]):
        base1= []
        rooms = 10
        beds = 8
        for room in range(rooms):
            if len(soldiers) > 0:
                for bed in range(beds):
                    base1.append(soldiers.pop(0))
        return base1
    
    def bases(soldiers: list[list[str]]):
        base_one = Residential_base.base_sorting(soldiers)
        base_two = Residential_base.base_sorting(soldiers)
        waiting = Residential_base.base_sorting(soldiers)
        return waiting


