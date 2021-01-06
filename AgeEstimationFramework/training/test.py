import argparse
import numpy as np
from matplotlib import pyplot as plt
import cv2
import os
import csv
from sklearn.metrics import mean_absolute_error

parser = argparse.ArgumentParser(description='Test')
parser.add_argument('--inputCSV',type=str,dest='csvtest',help='testset csv file')
parser.add_argument('--testFolder',type=str,dest='testfolder',help='testset folder')

args = parser.parse_args()
def cut(frame, roi):
    pA = ( int(roi[0]) , int(roi[1]) )
    pB = ( int(roi[0]+roi[2]-1), int(roi[1]+roi[3]-1) ) #pB will be an internal point
    W,H = frame.shape[1], frame.shape[0]
    A0 = pA[0] if pA[0]>=0 else 0
    A1 = pA[1] if pA[1]>=0 else 0
    data = frame[ A1:pB[1], A0:pB[0] ]
    if pB[0] < W and pB[1] < H and pA[0]>=0 and pA[1]>=0:
        return data
    w,h = int(roi[2]), int(roi[3])
    img = np.zeros((h,w,frame.shape[2]), dtype=np.float64)
    offX = int(-roi[0]) if roi[0]<0 else 0
    offY = int(-roi[1]) if roi[1]<0 else 0
    np.copyto(img[ offY:offY+data.shape[0], offX:offX+data.shape[1] ],data)
    return img

def mean_std_normalize(inp, means=None, stds=None):
    assert(len(inp.shape)>=3)
    d = inp.shape[2]
    if means is None and stds is None:
        means = []
        stds = []
        for i in range(d):
            stds.append( np.std(inp[:,:,i]) )
            means.append( np.mean(inp[:,:,i]) )
            if stds[i] < 0.001:
                stds[i] = 0.001
    outim = np.zeros(inp.shape)
    for i in range(d):
        if stds is not None:
            outim[:,:,i] = (inp[:,:,i] - means[i]) / stds[i]
        else:
            outim[:,:,i] = (inp[:,:,i] - means[i])
    return outim

def vggface2_preprocessing(img):
  ds_means = np.array([91.4953, 103.8827, 131.0912])
  ds_stds = None
  img = mean_std_normalize(img, ds_means, ds_stds)
  if (len(img.shape)<3 or img.shape[2]<3):
      img = np.repeat(np.squeeze(img)[:,:,None], 3, axis=2)
  return img

from tensorflow import keras
from keras_vggface.vggface import VGGFace
from keras.layers import Dense,Dropout,Flatten

m1 = VGGFace(model='resnet50', weights=None, input_shape=(224,224,3), classes=101,include_top=False)
#n = coremtools.convertes.keras.convert(model)
#n = keras.models.Model(input=model.input,output=model.output)
features = m1.layers[-1].output
x = Flatten()(features)
x = Dense(2048, activation='relu')(x)
x = Dropout(0.5)(x)
x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)
x = keras.layers.Dense(101, activation='softmax', use_bias=True, name='Logits')(x)

model = keras.models.Model(m1.input, x)


model.load_weights('/content/drive/Shareddrives/Exam/checkpoint.32.hdf5')
cnt=0
csv_reader=csv.reader(open(args.csvtest,mode='r'),delimiter=',')
csv_write=open('./csv_test_detected.csv',mode='w')
for row in csv_reader:
  cnt+=1
  print(cnt)
  image=row[2]
  ie=plt.imread(args.testfolder+'/'+image)

  im=vggface2_preprocessing(ie)
  ie = cut(im,[int(row[4]),int(row[5]),int(row[6]),int(row[7])])

  if (ie.shape[0] > 224 or ie.shape[1] >224):
    ie=cv2.resize(ie,(224,224))
  if (224-ie.shape[0])%2 ==1:
    top = int((224-ie.shape[0])/2)
    bottom = int((224-ie.shape[0])/2)+1
  else:
    top = int((224-ie.shape[0])/2)
    bottom = int((224-ie.shape[0])/2)

  if (224-ie.shape[1])%2 ==1:
    left= int((224-ie.shape[1])/2)
    right = int((224-ie.shape[1])/2)+1
  else:
    left = int((224-ie.shape[1])/2)
    right = int((224-ie.shape[1])/2)
  
  imag = cv2.copyMakeBorder(ie, top, bottom, left, right, cv2.BORDER_CONSTANT,value=0)
  jpg = np.reshape(imag, [1,imag.shape[0], imag.shape[1], imag.shape[2]])
  ris=np.argmax(model.predict(jpg))
  csv_write.write(image+','+str(ris)+'\n')
  
csv_write.close()

