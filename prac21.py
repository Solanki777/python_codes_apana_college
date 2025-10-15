# f = open ("demo.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","w")
# # here it will over write the content
# f.write("this the secrete code which is overwrited")
# f.close()

f =open("demo.txt","a")
f.write("\nthis is extra data which after the secreate data")
f.close