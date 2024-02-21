import os
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file in the Request'

    file = request.files['file']

    if file.filename == '':
        return 'No file selected'

    if file.filename[-4:] != '.bmp':
        return 'Selected file was not in .bmp type'

    filename = file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    return f'File {filename} successfully received and saved to ArmBoard'
    # return f'File {filename} successfully received and saved at {file_path}'

if __name__ == '__main__':
    app.run(debug=True)
