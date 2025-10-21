# how to access variable or method that are private in class .Now we have to access it from outside the class

class person:
    #private variable
    __acc_pin=34233
    def __bankpass(self):#private method
        print("i user your pass ****")

    def welcome(self):
        print("hello user")
        u1.__bankpass()
        pinNo=u1.__acc_pin
        return pinNo

u1=person()
pin=u1.welcome()
print("account pin number is reavled",pin)

# this how the private things are accessed here
