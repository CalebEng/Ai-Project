#Caleb Eng
#4/7/2023
#Messing with creating a discord chat bot


temp = "hello there My name is"

count= len(temp.split())
if count<20:
    for i in range(count, 20):
        temp+=" -"
print(temp)