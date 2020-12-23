# -------------------------------------------------------------------
# *
# * This module has been developed by Group 27 @ Artificial Vision DIEM.UNISA.
# *
# * Title:    generate_tf
# * Author:   Gargiulo, Marchesano, Sabini, Valitutto
# * Org.:     UNISA - DIEM - Artificial Intelligence - Artificial Vision - Group 27
# * Date:     23 Dic, 2020
# * -------------------------------------------------------------------

import csv
import tensorflow as tf
import os
import cv2

tfrecords_filename = '../tf_validation.record'
PATH="C:\\Users\\Andrew\\Desktop\\Contest_Artificial_Vision\\Dataset\\val"

writer = tf.io.TFRecordWriter(tfrecords_filename)

csv_train = open("../csv_train.csv", mode="r")
csv_reader = csv.reader(csv_train, delimiter=',')

def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def write_tfrecord(path_image,dict):
    """
    This funtion writes tfrecord file of train and validation data
    :param path_image: path of image to insert in tfrecord
    :param dict: dict containg match between identity and age
    :return:
    """
    cnt = 0
    for id in os.listdir(path_image):
        for jpg in os.listdir(path_image+"\\"+id):
            #img = Image.open(path_image+"/"+id+"/"+jpg)
            #width,height = img.size
            img = cv2.imread(path_image+"/"+id+"/"+jpg)
            is_success, im_buf_arr = cv2.imencode(".jpg", img)
            image_string = im_buf_arr.tobytes()
            image_shape = tf.image.decode_jpeg(image_string).shape
            #image_raw = img.tobytes()
            age = dict[id + "/" + jpg]
            example = tf.train.Example(features=tf.train.Features(feature={
                'height': _int64_feature(image_shape[0]),
                'width': _int64_feature(image_shape[1]),
                'image_raw': _bytes_feature(image_string),
                'label': _int64_feature(age)}))

            writer.write(example.SerializeToString())
        cnt+=1
        print(cnt)
    writer.close()


diz={}
with open('../csv_train.csv') as csv_file2:
	csv_reader = csv.reader(csv_file2, delimiter=',')
	for row in csv_reader:
		diz[row[0]] = int((row[1]))
print('Dict finished')

write_tfrecord(PATH,diz)
