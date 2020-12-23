# -------------------------------------------------------------------
# *
# * This module has been developed by Group 27 @ Artificial Vision DIEM.UNISA.
# *
# * Title:    read_tf_record
# * Author:   Gargiulo, Marchesano, Sabini, Valitutto
# * Org.:     UNISA - DIEM - Artificial Intelligence - Artificial Vision - Group 27
# * Date:     23 Dic, 2020
# * -------------------------------------------------------------------

from PIL import Image
import tensorflow as tf
from matplotlib import pyplot as plt
import io

string_record = 'tf_validation.record'

for record in tf.python.python_io.tf_record_iterator(string_record):

    example = tf.train.Example()
    example.ParseFromString(record)

    img_string = (example.features.feature['image_raw']
        .bytes_list
        .value[0])

    age = (example.features.feature['label']
        .int64_list
        .value[0])

    width = (example.features.feature['width']
        .int64_list
        .value[0])

    height = (example.features.feature['height']
        .int64_list
        .value[0])

    #img_1d = np.frombuffer(img_string, dtype=np.uint8)

    im = Image.open(io.BytesIO(img_string))
    #reconstructed_img = img_1d.reshape(height, width, -1)



    plt.imshow(im)
    plt.show()

    print(age,width,height)
'''
cnt=0
for record in tf.python.python_io.tf_record_iterator(string_record):
    cnt+=1
print(cnt)'''