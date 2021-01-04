import os
import csv

path_csv_crop = "C:\\Users\\Andrew\\Desktop\\train.detected.csv"

csv_total =csv.reader(open(path_csv_crop,mode="r"),delimiter=",")

diz_total = {}

for row in csv_total:
    diz_total[row[2]] = row

csv_test = csv.reader(open("../csv_test.csv",mode="r"),delimiter=",")

diz_test = {}

for row2 in csv_test:
    diz_test[row2[0]] = row2

csv_test = open("../csv_meta_test.csv",mode="w")

for id in diz_test.keys():
    csv_test.write(diz_total[id][0]+","+diz_total[id][1]+","+diz_total[id][2]+","
    +diz_total[id][3]+","+diz_total[id][4]+","+diz_total[id][5]+","+diz_total[id][6]
    +","+diz_total[id][7]+"\n")
