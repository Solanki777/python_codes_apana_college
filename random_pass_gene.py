import random
import string
# print(string.ascii_letters)
# # bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_uppercase)
# # ABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_lowercase)
# # abcdefghijklmnopqrstuvwxyz
# print(string.punctuation)
# # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~




t_string=string.punctuation+string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase+string.digits
# print(t_string)
passw=""
t_length=8
# for el in range(t_length):
#     passw += random.choice(t_string)

# to get in list formate
res=[random.choice(t_string) for i in range(t_length)]
print(res)

# print("your password is ",passw)




