try:
	import PIL
	import numpy as np
	import tensorflow as tf
	from tensorflow import keras
	from tensorflow.keras.optimizers import Nadam
	from tensorflow.keras.preprocessing.image import ImageDataGenerator
	import model
except ModuleNotFoundError:
	print('ERROR: Some of the required modules are missing')
	exit()

try:
	data_path = '../kaggle/data'
	generator = ImageDataGenerator(rescale=1./255, shear_range=0.3, zoom_range=0.3, horizontal_flip=True)
	data = generator.flow_from_directory(data_path, target_size=(160,160), batch_size=32, class_mode='categorical')
except FileNotFoundError:
	print('ERROR: Cannot find files containing data')
	exit()

cnn_model = model.build(output_types=2, activation='softmax', loss='log_cosh', optimizer=Nadam(learning_rate=0.0003))
cnn_model.summary()
cnn_model.fit(x=data, epochs=16)
cnn_model.save('brain_tumor_model.h5')