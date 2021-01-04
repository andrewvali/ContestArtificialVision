import csv
from shutil import copy2
import os

path_dataset ="C:\\Users\\Andrew\\Desktop\\Contest_Artificial_Vision\\train\\"
path_test = "C:\\Users\\Andrew\\Desktop\\Contest_Artificial_Vision\\Dataset\\test\\"


csv_test = csv.reader(open("../csv_test.csv",mode="r"),delimiter=",")

diz_id = {}
for row in csv_test:
    id = row[0][0:7]
    diz_id[id] = 1
'''
for key in diz_id.keys():
    os.mkdir(path_test + key)
'''
csv_test = csv.reader(open("../csv_test.csv",mode="r"),delimiter=",")

for row2 in csv_test:
    id = row2[0][0:7]
    p = row2[0][8:]
    copy2(path_dataset + id + "\\" + p, path_test + id + "\\" + p)
