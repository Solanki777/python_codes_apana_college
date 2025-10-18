# class car:
#     color="blue"
#     brand="TATA"

# car1=car()

# # when object is created the init function is called it called constructor

# car2=car()

# print(car1.color)
# print(f"{car1.brand} ", end= "\n\n" )
# print(car2.color)
# print(car2.brand)


# now using init function
# class car:

#     def __init__(self,fullname):
#         self.name=fullname
         
#         print("THIS IS NEW CAR ADDED BY TATA ")


# car1 = car("Maruti Suzuki")
# print(car1.name)

# car2= car("Nano")
# print(car2.name)

class student:
    name=anonymmous  #class attribute
    clgname="shantilal shah engineering college"
    # non parameterized constroctor
    def __init__(self):
        pass
    #  parameterized constructor
    def __init__(self, name,marks):
        self.name=name #object attribute which has higher priority than class attribute so it will print if some class attribute and object attribute name is same
        self.marks=marks
        print("addin new stdent data ...")

s1=student("Mahesh",100)
print(s1.name,s1.marks,s1.clgname)

s2=student("Montu",100)
print(s2.name,s2.marks)