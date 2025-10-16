# with open ("practice.txt","w") as f:
#     f.write("Hi everyone \nwe are learning File I\O\n")
#     f.write("using Java.\nI like programming in Java.")

# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data)
#     new_data=data.replace("Java","Python")
# with open("practice.txt","w") as f:
#     f.write(new_data)
    
# def check_for_word():
#     word="learning"
#     with open("practice.txt","r") as f:
#         data=f.read()
#         print(data.find(word) != -1)
#         if (data.find(word)) :
#             print("data not found")
#         else:
#             print("data found")

# check_for_word()

def check_for_line():
    
    with open("practice.txt","r") as f:
        word="learning"
        data=True
        line=1
        
        while data:
            data=f.readline()
            if word in data :
                return line
            else: 
                line +=1

        return -1
print(check_for_line())



