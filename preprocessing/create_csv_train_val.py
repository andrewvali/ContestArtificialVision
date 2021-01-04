# -------------------------------------------------------------------
# *
# * This module has been developed by Group 27 @ Artificial Vision DIEM.UNISA.
# *
# * Title:    create_csv_train
# * Author:   Gargiulo, Marchesano, Sabini, Valitutto
# * Org.:     UNISA - DIEM - Artificial Intelligence - Artificial Vision - Group 27
# * Date:     23 Dic, 2020
# * -------------------------------------------------------------------

import os
import csv
import numpy as np

# Path of training data
PATH_TO_TRAINING_DIR = "C:\\Users\\Andrew\\Desktop\\Contest_Artificial_Vision\\Dataset\\train\\"
PATH_CSV = "C:\\Users\\Andrew\\Desktop\\Contest_Artificial_Vision\\train.age_detected.csv"

diz={}
cnt = 0
with open(PATH_CSV) as csv_file2:
    csv_reader = csv.reader(csv_file2, delimiter=',')
    for row in csv_reader:
        diz[row[0]] = row
        diz[row[0]][1] = str(round(float(row[1])))
        cnt+=1

print('Dict finished')
print(cnt)

# csv file will contain annotations of train data
csv_data = open("../csv_train_val.csv", mode="w")

# Write csv_train.csv file
for id in os.listdir(PATH_TO_TRAINING_DIR):
    for image in os.listdir(PATH_TO_TRAINING_DIR+id):
        path_image = id+"/"+image
        csv_data.write(diz[path_image][0]+","+diz[path_image][1]+"\n")

cnt = 0
with open("../csv_train_val.csv") as csv_file3:
    csv_reader2 = csv.reader(csv_file3, delimiter=',')
    for row2 in csv_reader2:
        cnt+=1

print(cnt)
