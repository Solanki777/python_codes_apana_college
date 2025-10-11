num1=int(input("enter a numner 1:"))
num2=int(input("enter a numner 2:"))
num3=int(input("enter a numner 3:"))

if(num1>num2 and num1 >num3):
    print(num1,"is greater")
elif(num2>num3):
    print(num2,"is greater")
else:
    print(num3,"is greater")