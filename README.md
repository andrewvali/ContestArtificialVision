# ContestArtificialVision
This is the official repository of Artificial Vision exam.
## Team members
* Gargiulo Michele
* Marchesano Riccardo
* Sabini Pietro
* Valitutto Andrea

# Requirements
* Python 3.8
* Keras 2.0.6
* numpy == 1.18.4
* opencv-python == 4.2.0.34
* matplotlib == 3.2.1
* Keras == 2.3.1
* tensorflow-gpu == 1.14.0
* tqdm == 4.46.1 
  
## If you run the code on colab these requiriments are satisfied, but you will install the following packages:
* !pip install keras_applications
* !pip install keras_vggface

You will also need to download all the data for the datasets that you intend to use and extract it in the /content/Age_Estiamtion directory. You will find the annotation for vggface2 which includes the detected regions with the faces [here](https://github.com/MiviaLab/GenderRecognitionFramework/releases/tag/0), you will need to download the images separately from the official website.
The detection and the structure of the framework is the same of [GenderRecognitionFramework](https://github.com/MiviaLab/GenderRecognitionFramework) of [Mivia Lab](https://mivia.unisa.it/), but it is adapted to the problem of Age Estimation.
# Dataset
To split the entire dataset into train, validation and test set, run the following scripts:
* [preprocessing_original_dataset.py](https://github.com/andrewvali/ContestArtificialVision/blob/main/preprocessing/preprocessing_original_dataset.py): this script extract from entire dataset all images you want consider into 3 parts<br>
  * Set the correct path in [extract_images.py](https://github.com/andrewvali/ContestArtificialVision/blob/main/preprocessing/extract_images.py) file to specify where insert all images considered.
* [create_csv_train_val.py](https://github.com/andrewvali/ContestArtificialVision/blob/main/preprocessing/create_csv_train_val.py): This script writes the correct csv containing image path and label.
* [splitting_train_val.py](https://github.com/andrewvali/ContestArtificialVision/blob/main/preprocessing/splitting_train_val.py): This script takes the 80% of images for training and 20% for validation.
* [create_csv_splitted.py](https://github.com/andrewvali/ContestArtificialVision/blob/main/preprocessing/create_csv_splitted.py): This script writes the correct csv of training and validation part. 
* [delete_items.py](https://github.com/andrewvali/ContestArtificialVision/blob/main/preprocessing/delete_items.py): This script delete the validation from training.
* [test_set.py](https://github.com/andrewvali/ContestArtificialVision/blob/main/preprocessing/test_set.py): This script split the remaining part into a test set.
* [create_test_tar.py](https://github.com/andrewvali/ContestArtificialVision/blob/main/preprocessing/create_test_tar.py): Create the correct csv of test set.

Dataset distribution before and after splitting, is available [here](https://github.com/andrewvali/ContestArtificialVision/blob/main/csv_processing_analysis/Dataset_distribution.PNG)
# Train
In order to train neural networks, you must run ```train.py``` script from the training directory, available [here](https://github.com/andrewvali/ContestArtificialVision/blob/main/AgeEstimationFramework/training/train_AgeEstimation.py).
Here the used commands to train the associated paper solutions.
```bash
python3 train_AgeEstimation.py --net renset50 --dataset vggface2_gender --pretraining vggface2 --preprocessing vggface2 --augmentation vggface2 --batch 128 --lr 0.005 --training-epochs 50
```

* If you use colab it launches the cells of this [colab](https://github.com/andrewvali/ContestArtificialVision/blob/main/Resnet50.ipynb) step by step, adjusting the correct paths of the folders
* The implementation of Resnet50 is available [here](https://github.com/andrewvali/ContestArtificialVision/blob/main/AgeEstimationFramework/training/model_build.py) in the ```vggface_custom_build``` function.
# Evaluation
In order to evaluate the networks, move into the training directory and run the following command. In the subdirectory results, as the name suggests, you will find the results of these scripts in a csv file, where the first argument is the image and second command is age predicted by model.
```bash
python3 test.py --inputCSV path_test_csv --testFolder path_test_folder
```
* To see test.py, click [here](https://github.com/andrewvali/ContestArtificialVision/blob/main/AgeEstimationFramework/training/test.py)
* If you use colab it launches the cells of this [colab](https://github.com/andrewvali/ContestArtificialVision/blob/main/Resnet50.ipynb) step by step in the Test Network section, adjusting the correct paths of the folders
* To see the csv result, click [here](https://github.com/andrewvali/ContestArtificialVision/blob/main/Result/GROUP_27.csv)
# Project Structure
```
AgeEstimationFramework
├── dataset
│   ├── cache
│   ├── data
│   ├── face_models
│   ├── __pycache__
│   ├── face_detector.py
│   ├── vgg2_utils.py
│   └── vgg2_dataset_AgeEstimation.py      
├── trained
├── training
│   ├── corruptions.py
│   ├── __init__.py
│   ├── __pycache__
│   ├── keras-shufflenetV2
│   ├── keras-squeezenet
│   ├── cropout_test.py
│   ├── keras-squeeze-excite-network
│   ├── center_loss.py
│   ├── train_AgeEstimation.py
│   ├── model_build.py
│   ├── autoaug_test.py
│   ├── scratch_models
│   ├── dataset_tools.py
│   ├── keras-shufflenet
│   ├── keras_vggface
│   ├── DenseNet
│   ├── check_params.py
│   ├── autoaugment
│   └── ferplus_aug_dataset.py
├── Resnet50.ipynb
├── README.md
```
# Aknoweledgements
The code in this repository also includes open keras implementation of net Resnet50:
* VGGFace: [https://github.com/rcmalli/keras-vggface](https://github.com/rcmalli/keras-vggface)
# Note
Is it possible to view the model and the weights to the following [link](https://drive.google.com/drive/folders/17zIM0ftF_U4TgQ_wKIWz8pNfySlhps1r?usp=sharing)