import pandas as pd
import sqlite3 

class database():
    def __init__(self) -> None:
        self.conn = sqlite3.connect('person_data.db')
        self.c = self.conn.cursor()
        self.create_persontable()
        pass
    
    def create_persontable(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS persontable(gender TEXT,age TEXT, situation Text)')
    
    def add_persondata(self,gender,age,situation):
        self.c.execute('INSERT INTO persontable(gender,age,situation) VALUES (?,?,?)',(gender,age,situation))
        self.conn.commit()
    
    def view_all_person(self):
        self.c.execute('SELECT * FROM persontable')
        data = self.c.fetchall()
        return data
    
    def getAllData(self):
        user_result = self.view_all_person()
        clean_db = pd.DataFrame(user_result,columns=["Geschlecht","Alter","Lebenssituation"])
        return clean_db  


