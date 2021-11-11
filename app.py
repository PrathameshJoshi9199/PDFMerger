from flask import Flask

UPLOAD_FOLDER = 'C:/Users/Prathamesh.Joshi/Downloads/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTEXT_LENGTH'] = 16 * 1024 * 10
