class car:
    def __init__(self,type):
        self.type=type
    
    def start():
        print("car started..")

    def stop():
        print("car stopped")

class toyota(car):
    def __init__(self,name,type):
        # Now we can access the type method of parent 
        super().__init__(type)
        self.name=name
car1=toyota("prius","electric")
print(car1.type)