import csv
import os

path_csv = "C:\\Users\\Andrew\\Desktop\\train.detected.csv"
path_val = "C:\\Users\\Andrew\\Desktop\\Contest_Artificial_Vision\\Dataset\\train\\"

diz={}

csv_td=open(path_csv,mode="r")
reader = csv.reader(csv_td, delimiter=",")
cnt = 0
for row in reader:
    cnt+=1
    diz[row[2]] = row

print(cnt)

cnt = 0
with open("../csv_meta_train.csv",mode="w") as csv_val:
    for id in os.listdir(path_val):
        for image in os.listdir(path_val+id):
            cnt+=1
            path_image = id+"/"+image
            csv_val.write(diz[path_image][0]+","+diz[path_image][1]+","+diz[path_image][2]+","
                          +diz[path_image][3]+","+diz[path_image][4]+","+diz[path_image][5]
                          +","+diz[path_image][6]+","+diz[path_image][7]+"\n")


print(cnt)


'''
path_val = "C:\\Users\\Andrew\\Desktop\\Contest_Artificial_Vision\\Dataset\\val\\"
dict={}

csv_td=open("../csv_train.detected.csv",mode="r")
reader = csv.reader(csv_td, delimiter=",")
for row in reader:
    dict[row[2]] = row

csvtrain_final = open("../csv_train_final.csv",mode="r")
reader2 = csv.reader(csvtrain_final, delimiter=",")

csv_val = open("../csv_val.csv", mode="r")
reader3 = csv.reader(csv_val, delimiter=",")

with open("../csv_meta_train.csv",mode="w") as csv_meta_train:
    for row2 in reader2:
        try:
            rrow2 = dict[row2[0]]
            csv_meta_train.write(rrow2[0]+","+rrow2[1]+","+rrow2[2]+","+rrow2[3]+
					 ","+rrow2[4]+","+rrow2[5]+","+rrow2[6]+","+rrow2[7]+"\n")
        except:
            continue

with open("../csv_meta_val.csv",mode="w") as csv_meta_val:
    for row2 in reader3:
        try:
            rrow2 = dict[row2[0]]
            csv_meta_val.write(rrow2[0]+","+rrow2[1]+","+rrow2[2]+","+rrow2[3]+
					 ","+rrow2[4]+","+rrow2[5]+","+rrow2[6]+","+rrow2[7]+"\n")
        except:
            continue
'''