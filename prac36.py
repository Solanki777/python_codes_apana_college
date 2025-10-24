# getter and setters are methods used to access and update the attributes of a class. They provide controlled 

# class person:
#     def __init__(self,date):
#         # it is private data which can not access outside the class
#         self.__birthdate=date

# p1=person(2511)
# print(p1.__birthdate) #now it will throw the error because of private variable



class person:
    def __init__(self,date):
        self.__birthdate=date
    # getter method
    def get_birthdate(self):
        return self.__birthdate

p1=person(2511)
# print(p1.__birthdate)

# setter method
data=p1.get_birthdate()
print("data is given form setter method is",data)
