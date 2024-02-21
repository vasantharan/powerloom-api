import os
from flask import Flask, request

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'  # Folder where the uploaded files will be stored
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return 'No file in the Request'
    
    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return 'No file selected'

    if file[-4:] != '.bmg':
        return 'Selected file was not in .bmg type'
    # If file is successfully received, save it to the UPLOAD_FOLDER
    filename = file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    
    return f'File {filename} successfully received and saved at {file_path}'

if __name__ == '__main__':
    app.run(debug=True)
