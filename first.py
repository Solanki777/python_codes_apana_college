marks=int(input("enter your maarks out of 100:"))
if(marks>=90 and marks<=100):
    print("goodd")
elif(marks>=70 and marks<=100):
    print("average")
elif(marks>=45 and marks<=100):
    print("below average")
elif(marks<35 and marks>=0 ):
    print("you have do somthing")
else:
    print("fatal error")