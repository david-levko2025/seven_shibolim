from api.gen import app
from dal.residental_dal import beds_left
from api.csv_load import waiting_list


@app.get("/space/{residantal}")
def get_beds_by_res(residantal):
    response = beds_left(residantal)
    return response


@app.get("/waitingList")
def get_waiting_list(waiting):
    response = waiting_list(waiting)
    return response