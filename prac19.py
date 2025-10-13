def sum(num):
    if num==0:
        return 0
    else:
        return num +sum(num-1)

a=int(input("enter a number:"))
ans=sum(a)

print("Your answer is ",ans)