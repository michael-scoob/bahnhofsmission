import pandas as pd
import sqlite3 

class database():
    def __init__(self) -> None:
        self.conn_1 = sqlite3.connect('data/service_data.db',check_same_thread=False, isolation_level=None)
        self.c_1 = self.conn_1.cursor()
        self.create_table()
        pass
    
    def create_table(self):
        self.c_1.execute('CREATE TABLE IF NOT EXISTS persontable(daytime TEXT,gender TEXT,age TEXT, situation Text, leistung TEXT)')
    
    def addDataToTable(self,daytime,gender,age,situation,leistung):
        self.c_1.execute('INSERT INTO persontable(daytime,gender,age,situation,leistung) VALUES (?,?,?,?,?)',(daytime,gender,age,situation,leistung))
        self.conn_1.commit()
    
    def viewAllData(self):
        self.c_1.execute('SELECT * FROM persontable')
        data = self.c_1.fetchall()
        return data
    
    def clearAllData(self):
        self.c_1.execute('DELETE FROM persontable')
        self.conn_1.execute('VACUUM')
        self.conn_1.commit()
        return

    def getDataFrame(self):
        user_result = self.viewAllData()
        clean_db = pd.DataFrame(user_result,columns=["Zeit","Geschlecht","Alter","Lebenssituation","Leistung"])
        return clean_db  
