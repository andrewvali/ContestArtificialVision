# -------------------------------------------------------------------
# *
# * This module has been developed by Group 27 @ Artificial Vision DIEM.UNISA.
# *
# * Title:    get_ages_from_csv
# * Author:   Gargiulo, Marchesano, Sabini, Valitutto
# * Org.:     UNISA - DIEM - Artificial Intelligence - Artificial Vision - Group 27
# * Date:     23 Dic, 2020
# * -------------------------------------------------------------------

import os
import csv
import numpy as np

def read_csv(ages,path_csv):
    """
    This function read csv of path_csv
    :param ages: dict to match identity-age
    :param path_csv: csv to read
    :return: dict ages
    """
    with open(os.path.abspath(path_csv)) as csvfile:
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

