from flask_restful import Resource
from flask import request
from utils.classify import classify
import os
from werkzeug.utils import secure_filename

class HelloWorld(Resource):
    def get(self):
        # resp = {}
        # ui = []
        # for file in os.listdir('image_uploads'):
        #     ui.append(file)

        # resp['uploaded images']=ui
        return "hello"

    def post(self):
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save((os.path.join('./image_uploads', filename)))
        resp = classify(filename)

        # # remove uploaded files
        # for file in os.listdir('image_uploads'):
        #     os.remove('image_uploads/'+file)

        return(resp)

