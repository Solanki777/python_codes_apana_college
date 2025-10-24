class order:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    # this type of function where both side hase __ is called dunder function
    def __gt__(self,o2):
        return self.price >o2.price

o1=order("pasta",25)
o2=order("samosa",40)

print(o1<o2)