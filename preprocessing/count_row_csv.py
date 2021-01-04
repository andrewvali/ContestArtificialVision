import csv
import os
path = "C:\\Users\\Andrew\\Desktop\\Contest_Artificial_Vision\\train.age_detected.csv"

diz = {}
cnt = 0
with open("../csv_train.csv",mode="r") as csv_file:
    reader = csv.reader(csv_file,delimiter=",")
    for row in reader:
        diz[round(float(row[1]))]=0

with open("../csv_train.csv",mode="r") as csv_file2:
    reader2 = csv.reader(csv_file2,delimiter=",")
    for row2 in reader2:
        diz[round(float(row2[1]))] = diz[round(float(row2[1]))]+1

print(diz)
