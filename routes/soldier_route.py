from api.gen import app
from dal.soldier_dal import soldier_by_id_number
from api.csv_load import deployed_soldiers


@app.get("/search{id_number}")
def search_soldier_by_id_num(id_number):
    soldier_id_num = soldier_by_id_number(id_number)
    if soldier_id_num.deployed_soldiers:
             respone = f"the soldier id {soldier_id_num.id_number} deployed"
    else:
        respone =f"the soldier id {soldier_id_num.id_number} in waiting list"
    outcome = {"is deployed?": soldier_id_num.deployed_soldiers, "messege": respone}
    return outcome
    
