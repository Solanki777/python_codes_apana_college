class person():
    name="annoynomous"

    def changename(self,name):
        self.name=name

p1=person()
p1.changename("Shardha Khapra")
print(p1.name)

# it will give highe priority to class variables to print if there is class and method as same variable
print(person.name)
