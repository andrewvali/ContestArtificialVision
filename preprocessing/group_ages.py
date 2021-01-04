# -------------------------------------------------------------------
# *
# * This module has been developed by Group 27 @ Artificial Vision DIEM.UNISA.
# *
# * Title:    group_ages
# * Author:   Gargiulo, Marchesano, Sabini, Valitutto
# * Org.:     UNISA - DIEM - Artificial Intelligence - Artificial Vision - Group 27
# * Date:     23 Dic, 2020
# * -------------------------------------------------------------------

def group_ages(ages, grouped_ages, final_dict,partition):
    """
    This function divided ages of each identity in four group.
    Takes 150 image of each identity if type is train, 15 if type is validation (10% of train)

    :param ages: dict containig age of each identity
    :param grouped_ages: dict of four group of each identity
    :param final_dict: dict containing all image to take for each identity
    :param partition: train or validation
    :return: grouped_ages and final_dict
    """
    if partition in "train":
        MAX_JPGS = 30
    if partition in "validation":
        MAX_JPGS = 7

    for id in ages.keys():
        vals = list(ages[id].values())
        if len(vals)<=MAX_JPGS: #take all jpgs
            final_dict[id] = ages[id].keys()
        else:
            grouped_ages[id]={}
            grouped_ages[id]["group1"] = []
            grouped_ages[id]["group2"] = []
            grouped_ages[id]["group3"] = []
            grouped_ages[id]["group4"] = []
            cnt = -1
            min_val = min(vals)
            max_val = max(vals)
            r = max_val - min_val
            split = r//4
            for v in vals:
                cnt += 1
                if min_val<= v <min_val+split:
                    grouped_ages[id]["group1"].append(list(ages[id].keys())[cnt])
                elif min_val+split<= v <min_val+2*split:
                    grouped_ages[id]["group2"].append(list(ages[id].keys())[cnt])
                elif min_val+2*split<= v <min_val+3*split:
                    grouped_ages[id]["group3"].append(list(ages[id].keys())[cnt])
                else:
                    grouped_ages[id]["group4"].append(list(ages[id].keys())[cnt])
    return grouped_ages,final_dict