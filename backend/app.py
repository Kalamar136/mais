from flask import Flask, request
from flask_cors import CORS

import tensorflow as tf
import numpy as np
import keras
import cv2 as cv
from keras.preprocessing import image

app = Flask(__name__)
cors = CORS(app, resources={r'/*': {"origins": '*'}})
# app.config['CORS_HEADER'] = 'Content-Type'


@app.route('/upload', methods=['POST'])
def upload_file():
    formData = request.files.get('file','')
    print(type(formData))
    filestr = formData.read()
    #convert string data to numpy array
    npimg = np.fromstring(filestr, np.uint8)
# convert numpy array to image
    img = cv.imdecode(npimg, cv.IMREAD_COLOR)
    # img = formData.load_img(formData, target_size(128, 128))
    # x = image.img_to_array(img)
    # x = np.expand_dims(x, axis=0)
    print(img.shape)
    # print(request.file)
    # uploaded_file = request.files['file']
    # if uploaded_file.filename != '':
    #     uploaded_file.save(uploaded_file.filename)
    # return redirect(url_for('index'))
    return dict()

@app.route('/')
def simple():
    return dict()