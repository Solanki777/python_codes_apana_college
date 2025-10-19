# Abtraction: It is one of the 4 pillor of OOP where the only essential thing are shown other unnecessory data not show as below the bike shows start not how it start

class bike:
    def __init__(self):
        self.gear=False
        self.kick= False
        self.acc=False
        print("Do thing like kick,gear and acc then start")

    def start(self):
        self.gear=True
        self.kick=True
        self.acc=True
        # all check bike is starting
        print("Bike is starting ....")

# By creating object we encapsulate the data which is inside the funtion and class
b1=bike()
b1.start()