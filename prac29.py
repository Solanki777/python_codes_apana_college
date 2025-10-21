class student:
    def __init__(self,name,pas):
        self.name=name
        self.__acc_pass=pas 
        # put __ to make private variable which is limited within a class
s1=student("MR SOLANKI", "mr3443")

print(s1.name)
print(s1.__acc_pass)

del s1 #it will delete the object you created
# print(s1) 