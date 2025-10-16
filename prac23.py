# # with open("num.txt","w") as f:
# #     f.write("22,34,55,334,22,43,45,66,75,43,22,11,33,44,98")
# def check_num(n):
#     if(n%2==0):
#         print(f"{n} is even")
#         return 1
#     else:
#          print(f"{n} is odd")
#          return 0

# with open("num.txt","r") as f:
#     data=f.read()
#     print(data)

#     num=""
#     e=0
#     o=0
    
#     for i in range(len(data)):
#         if data[i]==",":
#             c=check_num(int(num))
#             if c== 1:
#                 e+=1
#             else :
#                 o+=1
#             num=""
#         else:
#             num+=data[i]

# print (f"even numbers:{e}")
# print (f"odd numbers:{o}")


#new method
with open ("num.txt","r") as f:
    data=f.read()
    print(data)
    e=0
    o=0
    num=data.split(",")
    print(num)
    for val in num:
        if (int(val) %2 == 0 ):
                e+=1
        else:o+=1
    print(f"even number {e}")
    print(f"odd number{o}")
