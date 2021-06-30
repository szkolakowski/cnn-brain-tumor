### cnn-brain-tumor
##### About
CNN Brain Tumor is a classic convolutional neural network, specifically trained for recognizing brain tumors on skull tomography scans. With prediction accuracy
of 94.74% it is rarely mistaken. In order to test the accuracy of the trained model, simply put some clean skull tomography scans (no additional text and arrows,
only bright skull on dark background) in `test/data` directory of the project. Script will show all images with calculated prediction written above. Projects uses
`try:` and `except:` functions to make sure all files are present.
##### Required Modules
In order to start a project you need to create a virtual environment with:\
*tensorflow*\
*keras*\
*numpy*\
*pillow*\
*matplotlib*
##### Kaggle
Kaggle folder contains a database of skull tomography scans with precise description of all files.\
Database found on https://www.kaggle.com/preetviradiya/brian-tumor-dataset
##### Test
Test folder contains `data` directory and `test.py` script.\
If you want to test trained model, simply put some photos in `data` directory and launch `test.py` script.\
The main objective of `test.py` is to extract all test data from the `data` directory, and prepare it for the model. Preparation is all about changing the
pixel width and height of an image, and then transfering it into a *numpy* array. After that, script loads the model from `../train/brain-tumor-model.h5` and
makes predictions with it. Every image will be displayed using *matplotlib.pyplot* with a result of `model.predict`.
##### Train
README not finished yet
