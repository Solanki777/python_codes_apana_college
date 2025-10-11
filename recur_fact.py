def factorial(fact):
    if fact==0 or fact==1:
        return 1
    else: 
        return fact * factorial(fact-1)

num=int(input("enter a number:"))
ans = factorial(num)
print("factorial of",num,"is ",ans)