
class person():
    def __init__(self, gender, age, situation, service) -> None:
        self.gender = gender
        self.age = age
        self.situation = situation
        self.service = service
    
    def getData(self):
        person=[
                "Geschlecht = " + self.gender, 
                "Alter = " +  self.age,
                "Lebenslage = "  + str(self.situation),
                "Leistung = "   + str(self.service) 
                
        ]
        return person