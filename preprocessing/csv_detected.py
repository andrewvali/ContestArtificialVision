import csv
import os

path_csv_cr = "C:\\Users\\Andrew\\Desktop\\train.detected.csv"
path_csv_validation = "../csv_train.csv"

csv_writer = open("../csv_train.detected.csv", mode="w")

diz={}
with open('../csv_train.csv') as csv_file2:
	csv_reader = csv.reader(csv_file2, delimiter=',')
	for row in csv_reader:
		diz[row[0]] = int((row[1]))
print('Dict finished')

diz2={}
with open(path_csv_cr) as csv_file3:
	csv_reader2 = csv.reader(csv_file3, delimiter=',')
	for row2 in csv_reader2:
		diz2[row2[2]] = row2
print('Dict finished')

for key in diz:
    print("djfn")
    csv_writer.write(diz2[key][0]+","+diz2[key][1]+","+diz2[key][2]+","+diz2[key][3]+
					 ","+diz2[key][4]+","+diz2[key][5]+","+diz2[key][6]+","+diz2[key][7]+"\n")

