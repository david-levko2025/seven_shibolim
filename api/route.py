from fastapi import UploadFile
import io
import csv
from models.residential_base import Residential_base
from functions.bublle_sort import Sort
from api.gen import app



@app.post("/assignWithCsv")
def upload_csv_plus_sort(file: UploadFile):
    if file.content_type != "text/csv":
         return {"error": "File must be a CSV"}
    
    content = file.file.read().decode("utf-8")
    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    rows = list(reader)
    Sort.sort_on_distance(rows)
    distribution_by_residence = Residential_base.bases(rows)
    deployed_soldiers = len(distribution_by_residence['base_one']) + len(distribution_by_residence['base_two']
                                                                         

    return {
        "the number of soldiers deployed ":deployed_soldiers,
        "the waiting": distribution_by_residence["waiting"]
    }








