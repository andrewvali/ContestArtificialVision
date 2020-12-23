# -------------------------------------------------------------------
# *
# * This module has been developed by Group 27 @ Artificial Vision DIEM.UNISA.
# *
# * Title:    delete_items
# * Author:   Gargiulo, Marchesano, Sabini, Valitutto
# * Org.:     UNISA - DIEM - Artificial Intelligence - Artificial Vision - Group 27
# * Date:     23 Dic, 2020
# * -------------------------------------------------------------------

import os

# path folder containg all data of dataset_processed
PATH_TO_DELETE = "C:\\Users\\Andrew\\Desktop\\Contest_Artificial_Vision\\Dataset_processed\\"
# path of validation folder
PATH_SOURCE = "C:\\Users\\Andrew\\Desktop\\Contest_Artificial_Vision\\Dataset_validation\\"

def delete_jpgs(path_to_delete,path_source):
    """
    This function deletes all jpgs of Dataset validation contained in dataset processed to create trianing folder
    :param path_to_delete: path to delete jpgs
    :param path_source: path of jpgs to delete
    :return: None
    """
    cnt = 0

    for id in os.listdir(path_source):
        for jpg in os.listdir(path_source+"/"+id):
            cnt += 1
            try:
                os.remove(path_to_delete+id+"\\"+jpg)
            except FileNotFoundError:
                print("File doesn't exist")
    print(cnt)
    print("Items Deleted!")

delete_jpgs(PATH_TO_DELETE,PATH_SOURCE)