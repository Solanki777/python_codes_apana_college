import random
target= random.randint(1,100)
q="a"

while True:
    if q=="Q":
        break
    key=int(input("enter a key value to find:"))
   
    if target==key:
        print("key is found")
        break
    elif(target<key):
        print("key is bigger than expected")
    
    else:
        print("key is smaller than expected")
    q=str(input("If you want to quite press Q:"))


print("--GAME OVER--")