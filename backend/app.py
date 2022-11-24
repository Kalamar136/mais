from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r'/*': {"origins": '*'}})
# app.config['CORS_HEADER'] = 'Content-Type'


@app.route('/upload', methods=['POST'])
def upload_file():
    formData = request.files.get('file','')
    print(type(formData))
    formData.save('image.jpg')
    print(formData)
    # print(request.file)
    # uploaded_file = request.files['file']
    # if uploaded_file.filename != '':
    #     uploaded_file.save(uploaded_file.filename)
    # return redirect(url_for('index'))
    return dict()

@app.route('/')
def simple():
    return dict()