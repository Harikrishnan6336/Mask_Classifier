# 😷Mask Classifier

A Binary Image Classification in PyTorch classifying faces as with or without wearing masks. 

This project was done as part of my PyTorch learning as part of [TinkerHub](https://tinkerhub.org/)'s [ComputerVision with PyTorch Learning Program](https://github.com/tinkerhub-org/ComputerVision-with-PyTorch-Learning-Program).  



## 📘 Description

A simple binary image classification using the deep learning framework PyTorch that can classify faces as with or without wearing masks. 

The dataset used can be found [here](https://github.com/prajnasb/observations/tree/master/experiements/data). 

The dataset contains a total of 816 images which includes 408 images each in both categories. More images are added to the training set with Image Augmentation. The number of training images(After Image Augmentation) used is 1956 and the number of test images is 164. The images are  given in the zip file [here](https://github.com/Harikrishnan6336/Mask_Classifier/blob/master/data/images.zip). They are named in numerical order for the sake of convenience([image_namer.py](https://github.com/Harikrishnan6336/Mask_Classifier/blob/master/data/image_namer.py) is used for naming the images). The name of the images along with thier labels are in [mask.csv](https://github.com/Harikrishnan6336/Mask_Classifier/blob/master/csv/mask.csv) file([make_csv.py](https://github.com/Harikrishnan6336/Mask_Classifier/blob/master/csv/make_csv.py) is used for making the csv file).

Two models are trained:- 
One using the Convolutional Neural Networks and the other one is trained on the VGG16 model by applying **transfer learning**. The model weights of the VGG16 model is freezed and a Linear layer is added to its end and the data is trained on it. 

The entire code was run and tested in Google [colab](https://colab.research.google.com/notebooks/intro.ipynb#recent=true)


The source code with little changes can be used to tackle any binary image classification.



#### 🎯 Test Accuracy  
 obtained by the
 
 CNN model  - 89.40%
 
 VGG16 model - 82.34%



## Built With ❤️ 

* [Python3.6](https://docs.python.org/3.6/) - The Programming language used
* [PyTorch](https://pytorch.org/) - The deep learning framework used
* [VGG16](https://github.com/pytorch/vision/blob/master/torchvision/models/vgg.py) - A pretrained CNN which is trained on the [ImageNet](http://www.image-net.org/) dataset. 


## 💁🏻 Contributing
[![Contributors][contributors-shield]][contributors-url]

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. 🍴 Fork the Project
2. Create your Feature Branch (`git checkout -b feature/newFeature`)
3. Commit your Changes (`git commit -m 'Add some newFeature'`)
4. Push to the Branch (`git push origin feature/newFeature`)
5. Open a Pull Request

Please feel free to raise any issue...


 


[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/Harikrishnan6336/Mask_Classifier/graphs/contributors
