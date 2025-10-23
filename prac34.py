# class student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         self.percentage=str(( self.phy+self.math+self.chem)/3) + "%"

# s1=student(98,99,97)
# print(s1.percentage)

# Now after some time teacher knows that physics mark is wrong so he will try to change like this

# s1.phy=76
# print(s1.percentage)
# you can see it prints the same because when first time user passes the value it calclate and store the result but after that when user made some change in marks it will not do any calculation without calling the function or constructor


# 1 Solution:

# class student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         # self.percentage=str(( self.phy+self.math+self.chem)/3) + "%"

#     def cal(self):
#         return (str((self.phy+self.math+self.chem)/3))+"%"
        
# s1=student(98,99,97)
# print(student.cal(s1))

# s1.phy=76
# print(student.cal(s1))


# but envery time calling that function is where handfull so we can user property keyword which will cal all data again we change any internal assets

# other solution: 
class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        # self.percentage=str(( self.phy+self.math+self.chem)/3) + "%"
    @property
    def cal(self):
        return str((self.phy+self.math+self.chem)/3)+"%"
        
s1=student(98,99,97)
print(s1.cal)

s1.phy=76
print(s1.cal)
