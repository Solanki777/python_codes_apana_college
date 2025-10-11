# # 1 and 2
# heros=["ironman","loki","captain america","thor","hulk","balck widow"]
# anime_char=["Naruto","Monkey.D.Luffy","Bankai","Goku","Sung-jin-woo","Kira","Zoro","Itachi"]

# def length(list):
#     print(len(list))

# def insigleline(list):
#     for el in list:
#         print (el,end=" ")


# length(heros)
# length(anime_char)
# insigleline(heros)
# insigleline(anime_char)


# 3. 
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=i*f
#     return f

# num=int(input("enter a number:"))
# ans=fact(num)
# print("factorial of " ,num ,"is" ,ans)

# # 4.
# def convertor(USD):
#     return USD*88.75
# U=int(input("enter usdt:"))
# print(U,"'s price is ",convertor(U))

#hw

def chek(n):
    if n==0: return "ZERO" 
    elif n<0 : return "NAGATIVE"
    elif n%2==0 :
        return "ENVEN"
    else:
        return "ODD"
n=int(input("enter a number:"))
print("number is",chek(n))