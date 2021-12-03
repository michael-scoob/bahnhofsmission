import pandas as pd
import sqlite3 

class database():
    def __init__(self) -> None:
        self.conn_1 = sqlite3.connect('person_data.db')
        self.c_1 = self.conn_1.cursor()
        self.create_persontable()
        pass
    
    # Peronen und Service DB
    def create_persontable(self):
        self.c_1.execute('CREATE TABLE IF NOT EXISTS persontable(daytime TEXT,gender TEXT,age TEXT, situation Text, leistung TEXT)')
    
    def add_persondata(self,daytime,gender,age,situation,leistung):
        self.c_1.execute('INSERT INTO persontable(daytime,gender,age,situation,leistung) VALUES (?,?,?,?,?)',(daytime,gender,age,situation,leistung))
        self.conn_1.commit()
    
    def view_all_person(self):
        self.c_1.execute('SELECT * FROM persontable')
        data = self.c_1.fetchall()
        return data
    
    def getAllData(self):
        user_result = self.view_all_person()
        clean_db = pd.DataFrame(user_result,columns=["Zeit","Geschlecht","Alter","Lebenssituation","Leistung"])
        return clean_db  
