from fastapi import UploadFile,FastAPI
import io
import csv
import uvicorn
from models.residential_base import Residential_base
from functions import bublle_sort
app = FastAPI()

@app.post("/assignWithCsv")
def upload_csv(file: UploadFile):
    if file.content_type != "text/csv":
         return {"error": "File must be a CSV"}
    
    content = file.file.read().decode("utf-8")
    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    rows = list(reader)
    bublle_sort.sorted_by_distance(rows)
    distribution_by_residence = Residential_base.bases(rows)
    mm = len(distribution_by_residence)
    for line in rows:
        print(line)

    return ""






if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


