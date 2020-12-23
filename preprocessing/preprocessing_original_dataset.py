# -------------------------------------------------------------------
# *
# * This module has been developed by Group 27 @ Artificial Vision DIEM.UNISA.
# *
# * Title:    preprocessing_original_dataset
# * Author:   Gargiulo, Marchesano, Sabini, Valitutto
# * Org.:     UNISA - DIEM - Artificial Intelligence - Artificial Vision - Group 27
# * Date:     23 Dic, 2020
# *
# * This module splits the original dataset into a specific sub-group
# * -------------------------------------------------------------------

from get_ages_from_csv import read_csv
from group_ages import group_ages
from recover_identities import recover_identities
from plot_utils import vs_plot
from extract_images import extract_jpgs

ages = {}  # {identity:{jpg:age}}
grouped_ages = {} #{identity:{group_age:[jpgs]}}
final_dict = {} #{identity:jpgs}
splitted_dict_samples, splitted_dict_labels = {},{}

print("Getting ages...")
ages = read_csv(ages)
print("Getting ages... DONE")

print("Grouping ages...")
grouped_ages, final_dict = group_ages(ages, grouped_ages, final_dict,"train")
print("Grouping ages... DONE")

print ("Recovering identities from groups...")
final_dict = recover_identities(grouped_ages,final_dict,"train")
print ("Recovering identities from groups...DONE")

print("NUMBER OF TAKEN IDENTITIES: {}".format(len(final_dict.keys()))) #8421
cnt = 0
for jpgs in final_dict.values():
    cnt += len(jpgs)
print("NUMBER OF TAKEN SAMPLES: {}".format(cnt)) #1261462

# Check the correct path in extract_jpgs file
extract_jpgs(final_dict)

print ("Plotting...")
vs_plot(ages, final_dict, splitted_dict_labels)
print ("Plotting...DONE")

