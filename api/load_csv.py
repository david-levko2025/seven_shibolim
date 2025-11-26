import csv
from io import StringIO
from models.info_soldiers import Soldier

class SoldierCSV:
    def __init__(self, file):
        self.file = file
        self.soldiers = []

    def load(self):
        decoded = self.file.read().decode('utf-8')
        reader = csv.DictReader(StringIO(decoded))
        for row in reader:
            soldier = Soldier(id_number=int(row['id_number']), f_name=row['f_name'], l_name=row['l_name'],gender=row['gender'],city = row['city'],distance=row['distance'],status=bool(row['status']))
            self.soldiers.append(soldier)