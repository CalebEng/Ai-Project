#Caleb Eng
#4/7/2023
#Messing with creating a discord chat bot


import csv

with open('Data set/conversation_enc.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count =0
    for row in csv_reader:
        if line_count ==0:
            print(f"Column names are {', '.join(row)}")
            line_count+=1





