import csv
import os
import numpy as np

csv_raeder = open("../csv_train_final.csv",mode="r")
reader = csv.reader(csv_raeder,delimiter = ",")

diz_total = {}

ages_array = np.zeros(101)

cnt = 0
for row in reader:
    diz_total[row[0]] = row[1]

csv_train =  open("../csv_train.csv",mode="r")
reader_train = csv.reader(csv_train,delimiter = ",")

diz_train ={}
for row2 in reader_train:
    diz_train[row2[0]] = row2

csv_val =  open("../csv_val.csv",mode="r")
reader_val = csv.reader(csv_val,delimiter = ",")

diz_val ={}
for row3 in reader_val:
    diz_val[row3[0]] = row3

diz_test = {}
for key in diz_total.keys():
    if diz_train.get(key) == None and diz_val.get(key) == None and ages_array[int(diz_total[key])]<400:
        diz_test[key] = diz_total[key]
        ages_array[int(diz_total[key])]+=1

diz_ages = {}
cnt = 0
for i in range(0,101):
    diz_ages[i] = ages_array[i]
    cnt+=ages_array[i]

print(diz_ages)
print(cnt)

csv_w = open("../csv_test.csv",mode="w")

for k in diz_test.keys():
    csv_w.write(k+","+diz_test[k]+"\n")
