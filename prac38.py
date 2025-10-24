class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return self.radius*22/7*22/7
    def perimeter(self):
        return 2*22/7*self.radius
    
c1 = circle(7)
print("area of circle is ",c1.area())
print("perimter of circle is",c1.perimeter())