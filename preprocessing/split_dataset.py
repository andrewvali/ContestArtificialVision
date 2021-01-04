import csv
from collections import Counter

path_csv = "C:\\Users\\Andrew\\Desktop\\Contest_Artificial_Vision\\train.age_detected.csv"

diz={}
list = []
with open(path_csv,mode="r") as csv_file:
    reader = csv.reader(csv_file,delimiter=",")
    for row in reader:
        diz[row[0]] = row
        list.append(round(float(row[1])))

print(Counter(list))