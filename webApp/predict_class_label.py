import pandas as pd
import numpy as np
import pickle

import keras

from os.path import join as pjoin
from os import path
from PIL import Image

np.random.seed(25)


IMAGE_PATH = './static/upload'
MODEL_META = './static/model_meta'

def read_image(img_path = None):
    
    relative_image_path = pjoin(IMAGE_PATH, img_path)

    print(relative_image_path) 
    
    img = Image.open(relative_image_path)
    
    if img.size != (24,40):
        raise ValueError("{} image needs resizing".format(img_path))
    
    arr = np.array(img)
    
    arr = arr.reshape((arr.shape[0], arr.shape[1], 1))
    
    return arr

def prediction(test_image_path = None):
    
    test_image_array = []
    
    test_image = read_image(img_path = test_image_path)
        
    test_image_array.append(test_image)
    test_image_array = np.array(test_image_array)
    
    print(test_image_array.shape)
    
    test_image_array = test_image_array.astype('float32')
    
    test_image_array/=255
    
    model = keras.models.load_model(pjoin(MODEL_META,'JUA_baseline.h5'))
    
    prediction = model.predict_classes(test_image_array)
    
    prediction_prob = np.round(model.predict_proba(test_image_array)[0][prediction][0]*100,2)
    
    pickle_file = open(pjoin(MODEL_META, "label_encoder.pkl"), "rb")
    
    label_encoder = pickle.load(pickle_file)
    
    prediction = label_encoder.inverse_transform(prediction)
    
    return prediction[0], prediction_prob