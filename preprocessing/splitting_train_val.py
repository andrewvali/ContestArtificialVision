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
from preprocessing.plot_utils import vs_plot
from recover_identities import recover_identities
from extract_images import extract_jpgs

ages={}
grouped_ages = {}
final_dict = {}
splitted_dict_labels = {}

ages = read_csv(ages, "../csv_train_val.csv")
print("Ages read")

grouped_ages, final_dict = group_ages(ages, grouped_ages, final_dict,'validation')

final_dict = recover_identities(grouped_ages,final_dict,"validation")

print("NUMBER OF TAKEN IDENTITIES: {}".format(len(final_dict.keys()))) #8421
cnt = 0
for jpgs in final_dict.values():
    cnt += len(jpgs)
print("NUMBER OF TAKEN SAMPLES: {}".format(cnt)) #1261462

# Check the correct path in extract_jpgs file
extract_jpgs(final_dict)
print("jpgs extracted")
print ("Plotting...")
vs_plot(ages, final_dict, splitted_dict_labels)
print ("Plotting...DONE")
