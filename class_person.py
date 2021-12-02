
class person():
    def __init__(self, gender, age,situation) -> None:
        self.gender = gender
        self.age = age
        self.situation = situation
    
    def getData(self):
        person=[
                "Geschlecht: " + self.gender, 
                "Alter: " +  self.age,
                "Situation: "  + str(self.situation)
        ]
        return person