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