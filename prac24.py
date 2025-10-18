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
class car:

    def __init__(self,fullname):
        self.name=fullname
         
        print("THIS IS NEW CAR ADDED BY TATA ")


car1 = car("Maruti Suzuki")
print(car1.name)

car2= car("Nano")
print(car2.name)