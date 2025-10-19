# class student:
#     def __init__(self,name):
#         self.name=name
#         print("added one student name")

#     def average(self,m1,m2,m3):
#         return (m1+m2+m3)/3

# s1=student("mahesh")
# print(s1.name)
# ans=s1.average(98,97,67)

# print(f"the average marks of student {s1.name} is {ans}")

# By apna college
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hy",self.name,"your avg score is:",sum/3)


s1=student("Tony Stark", [99,97,67])
s1.get_avg()