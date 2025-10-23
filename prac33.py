class person():
    name="annoynomous"

    # def changename(self,name):
    #     self.name=name
    #     # self.__class__.name="Shardha khapra"
    #     # it will chnge class variable
    
    # it also can access class varible 
    @classmethod
    def changename(cls,name):
        cls.name=name


p1=person()
p1.changename("Shardha Khapra")
print(p1.name)

# it will give highe priority to class variables to print if there is class and method as same variable
print(person.name)
