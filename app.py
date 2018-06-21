from flask import Flask
from flask_restful import Api
from endpoints.Main import *

UPLOAD_FOLDER = '/image_uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
api = Api(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)