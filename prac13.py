i=1
while i<=100:
    print(i)
    i+=1
print("loop ended\n")

while i>=0:
    print(i)
    i-=1
print("loop ended\n")

i=1
t=int(input("ente a number:"))
while i<=10:
    print(t,"*",i,"=",t*i)
    i+=1
print("loop ended\n")

a=[]
i=1
while i<=10:
    a.append(i**2)
    i+=1
print(a)

a=(34,23,45,56,67,13,34,56)
i=0
while i<len(a):
    if a[i]==34:
        print("found at :",i,",")
    i+=1

    



