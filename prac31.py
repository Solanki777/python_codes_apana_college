class school:
    @staticmethod
    def schools_has():
        print("we have fine staff to do anything")

    @staticmethod
    def schools_services():
        print("we provide best services to student")

# it is proprety of inheritence where the properties of class menthion as below is pass from parent to its child. Here parent is school and child is M.D.Shah
class M_D_Shah(school):
    def __init__(self,steam):
        self.steam=steam

s1=M_D_Shah("Science")
print(s1.steam)
print(s1.schools_has())
print(s1.schools_services())