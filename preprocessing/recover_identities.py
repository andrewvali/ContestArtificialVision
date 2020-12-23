# -------------------------------------------------------------------
# *
# * This module has been developed by Group 27 @ Artificial Vision DIEM.UNISA.
# *
# * Title:    recover_identities
# * Author:   Gargiulo, Marchesano, Sabini, Valitutto
# * Org.:     UNISA - DIEM - Artificial Intelligence - Artificial Vision - Group 27
# * Date:     23 Dic, 2020
# * -------------------------------------------------------------------

import random as rd

# GROUPED_AGES => {identity:{group_age:[jpgs]}} = {str:{str:list<str>}}
# FINAL_DICT #{identity:jpgs}

N_GROUPS = 4

rd.seed(42)

def recover_identities(grouped_ages,final_dict,partition):
    """
    This function takes images for each identity.
    Takes 150 image if partition is train, 15 if partition is validation
    :return:
    """
    if partition in "train":
        THRESHOLD = 30
        DELTA = 30
    if partition in "validation":
        THRESHOLD = 3
        DELTA = 3

    for id in grouped_ages.keys():
        remaining_jpgs = []
        adjust = False
        to_retrieve = 0
        final_dict[id] = []
        for i in range(1, N_GROUPS+1):
            try:
                jpgs = grouped_ages[id]["group{}".format(i)]
            except:
                print(id)
            if i == 3:
                if len(jpgs)>THRESHOLD+DELTA:
                    # take random 30 or 60 elements
                    sampling = rd.sample(jpgs, k=THRESHOLD+DELTA)
                    final_dict[id].extend(sampling)
                    for s in sampling:
                        jpgs.remove(s)
                    remaining_jpgs.extend(jpgs)
                else:
                    final_dict[id].extend(jpgs)
                    adjust = True
                    to_retrieve += THRESHOLD+DELTA - len(jpgs)
            elif len(jpgs) > THRESHOLD:
                # take random 30 elements
                sampling = rd.sample(jpgs, k=THRESHOLD)
                final_dict[id].extend(sampling)
                for s in sampling:
                    jpgs.remove(s)
                remaining_jpgs.extend(jpgs)
            else:  # take all
                final_dict[id].extend(jpgs)
                adjust = True
                to_retrieve += THRESHOLD - len(jpgs)
        if adjust:
            # partition = train: if a group hasn't 30 values, take the remaining values to reach 150 samples from remaining groups
            # partition = validation: if a group hasn't 3 values, take the remaining values to reach 15 samples from remaining groups
            sampling = rd.sample(remaining_jpgs, k=to_retrieve)
            final_dict[id].extend(sampling)
    
    return final_dict
