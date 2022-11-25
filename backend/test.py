import tensorflow as tf

from tf import keras

model2 = keras.models.load_model('model.txt')

# import pandas as pd
import cv2 as cv
# from PIL import Image

img = cv.imread('/content/drive/MyDrive/Garbage_photos/cardboard.jpg')
img = img.resize((128,128))
img.display()
#print(image)

model2.predict(img)

