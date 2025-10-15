# first creat demo.txt file than run this programs because i delete that file at last line of codes


# f = open ("demo.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","w")
# # here it will over write the content
# f.write("this the secrete code which is overwrited")
# f.close()

# f =open("demo.txt","a")
# f.write("\nthis is extra data which after the secreate data")
# f.close

#using with you dont have to close the file because it automaticalyy has been closed

# with open ("demo.txt","r") as f:
#     data=f.read()
#     print(data)

import os 
os.remove("demo.txt")