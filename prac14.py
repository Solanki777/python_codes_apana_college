lis=[1,4,9,16,25,49,64,81,100]

for l in lis:
    print(l)

x=int(input("enter a number:"))
ind=0
for l in lis:
    if l==x:
        print("number found ",ind)
    ind+=1


