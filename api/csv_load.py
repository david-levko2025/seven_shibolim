from fastapi import UploadFile
import io
import csv
from util.residential_base import Residential_base
from util.bublle_sort import Sort
from api.gen import app
from sqlmodel import Session
from dal.engine import engine
from models.info_soldiers import Soldier


def read_csv(content):
    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    rows = list(reader)
    return rows

@app.post("/assignWithCsv")
def upload_csv(file: UploadFile):
    if file.content_type != "text/csv":
         return {"error": "File must be a CSV"}
    
    content = file.file.read().decode("utf-8")
    rows = read_csv(content)
    with Session(engine) as session:
        for line in rows:
            soldier = Soldier(id_number = line[0],
                             f_name = line[1],
                             l_name = line[2],
                             gender = line[3],
                             city = line[4],
                             his_distance = line[5],
                             )
            session.add(soldier)
            session.commit()
            
    
    Sort.sort_on_distance(rows)
    distribution_by_residence = Residential_base.bases(rows)
    deployed_soldiers = len(distribution_by_residence['base_one']) + len(distribution_by_residence['base_two'])
    waiting_list = len(distribution_by_residence["waiting list"])


    return {
        "the number of soldiers deployed ":deployed_soldiers,
        "the waiting": distribution_by_residence["waiting"]
    }








