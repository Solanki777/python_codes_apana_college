class employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    
    def show(self):
        print(f"My role is {self.role} from {self.department} and my salary is {self.salary} ")

e1=employee("BUG BOUNTY HUNTER","IT",40000)
e1.show()