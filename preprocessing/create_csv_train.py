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
PATH_TO_TRAINING_DIR = "C:\\Users\\Andrew\\Desktop\\Contest_Artificial_Vision\\Dataset_processed\\"

def read_csv(ages):
    """
    This function read csv containing all data and creates a match between identity and age
    :param ages: dict containing age for each identity
    :return: dict ages
    """
    with open(os.path.abspath("train.age_detected.csv")) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ')
        for row in csvreader:
            split = row[0].split(",")
            file_path = split[0]
            identity = file_path[:7]
            try:
                d = ages[identity]
            except:
                ages[identity] = {}
            jpg = file_path[7:]
            age = np.round(float(split[1]))
            ages[identity][jpg] = age
    return ages

# csv file will contain annotations of train data
csv_data = open("../csv_train.csv", mode="w")
# csv of all data
csv_train = open("train.age_detected.csv", mode="r")
csv_reader = csv.reader(csv_train, delimiter=',')

# Write csv_train.csv file
for id in os.listdir(PATH_TO_TRAINING_DIR):
    for image in os.listdir(PATH_TO_TRAINING_DIR+"/"+id):
        path_image = id+"/"+image
        #print(path_image)
        for row in csv_reader:
            #print(row[0][:19])
            #print(path_image)
            if path_image in row[0][:19]:
                csv_data.write(path_image+","+str(round(int(row[1])))+"\n")
                break
