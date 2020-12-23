# -------------------------------------------------------------------
# *
# * This module has been developed by Group 27 @ Artificial Vision DIEM.UNISA.
# *
# * Title:    extract_images
# * Author:   Gargiulo, Marchesano, Sabini, Valitutto
# * Org.:     UNISA - DIEM - Artificial Intelligence - Artificial Vision - Group 27
# * Date:     23 Dic, 2020
# * -------------------------------------------------------------------
import os
from shutil import copy2

# Path containg all data
PATH_TO_EXTRACT_DATASET = "C:\\Users\\Andrew\\Desktop\\Contest_Artificial_Vision\\train\\"
# New path of training data
PATH_TO_TRAINING_DIR = "C:\\Users\\Andrew\\Desktop\\Contest_Artificial_Vision\\Dataset_processed\\"


def extract_jpgs(splitted_dict_samples): #{id:{"train":[jpgs]}}
    """
    This function copies jpgs files from PATH_TO_EXTRACT_DATASET into PATH_TO_TRAINING_DIR
    :param splitted_dict_samples: dict containing all jpgs of training
    :return: None
    """
    cnt = 0

    print("Extracting to {}...".format(PATH_TO_TRAINING_DIR))

    ids = list(splitted_dict_samples.keys())
    ids.sort()
    for id in ids:
        os.mkdir(PATH_TO_TRAINING_DIR + id)
        jpgs = list(splitted_dict_samples[id])
        jpgs.sort()
        for jpg in jpgs:
            cnt += 1
            src = PATH_TO_EXTRACT_DATASET + id + jpg    # train/id/jpg
            dst = PATH_TO_TRAINING_DIR + id + jpg       # training_set/id/jpg
            copy2(src, dst)

    print(cnt)
    print("Extracting...DONE")


