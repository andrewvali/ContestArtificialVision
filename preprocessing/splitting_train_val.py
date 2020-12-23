# -------------------------------------------------------------------
# *
# * This module has been developed by Group 27 @ Artificial Vision DIEM.UNISA.
# *
# * Title:    splitting_train_val
# * Author:   Gargiulo, Marchesano, Sabini, Valitutto
# * Org.:     UNISA - DIEM - Artificial Intelligence - Artificial Vision - Group 27
# * Date:     23 Dic, 2020
# *
# * This module implements the division of dataset in training and validation
# * -------------------------------------------------------------------

from group_ages import group_ages
from get_ages_from_csv import read_csv
from recover_identities import recover_identities
from extract_images import extract_jpgs

ages={}
grouped_ages = {}
final_dict = {}

ages = read_csv(ages, "../csv_train.csv")
print("Ages read")

grouped_ages, final_dict = group_ages(ages, grouped_ages, final_dict)

final_dict = recover_identities(grouped_ages,final_dict,"validation")

# Check the correct path in extract_jpgs file
extract_jpgs(final_dict)
print("jpgs extracted")
