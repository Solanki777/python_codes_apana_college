# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def __show__(self):
#         return f"{self.real}i +{self.img}j"
    
    


# num1=complex(45,58)
# print(num1.__show__())
# num2=complex(66,78)
# print(num2.__show__())

# # it will through error because it can not do some like this
# sum=num1+num2

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return complex(newreal,newimg)

num1=complex(45,15)
num1.show()

num2=complex(435,125)
num2.show()

num3=num1+num2
num3.show()