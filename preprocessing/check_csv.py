import os
import pickle
import numpy as np
import csv
path_train_cache = "C:\\Users\\Andrew\\Desktop\\test_dataset\\vggface2_gender_train.cache"
path_val_cache = "C:\\Users\\Andrew\\Desktop\\test_dataset\\vggface2_gender_val.cache"

objects = []
objects2 = []
'''
with (open("../vggface2_gender_val.cache", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break

print(objects[0][0]['label'])
for el in objects[0]:
    lb = el['label']
    alb = np.zeros(101)
    alb[lb] = 1
    el['label'] = alb

print(objects[0][0]['label'])


with (open("../vggface2_gender_val.cache", "rb")) as openfile:
    while True:
        try:
            objects2.append(pickle.load(openfile))
        except EOFError:
            break

print(len(objects))
print(len(objects2))
print(objects[0][0][0])
print(objects2[0][0][0])


cnt = 0
new_objects = []
#new_objects.append([])
for el in objects[0]:
    if cnt%2 == 0:
        new_objects.append(el)
    cnt+=1


print(len(objects[0][1]))
print(len(new_objects[0]))

with open("../vggface2_gender_val.cache", 'wb') as f:
    print("Pickle dumping")
    pickle.dump(objects, f)
'''

