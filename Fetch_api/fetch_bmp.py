import os
from flask import Flask, request, jsonify
from flask_cors import CORS
# from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client['powerloom_db']
# collection = db['powerloom_collection']

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file in the Request'

    file = request.files['file']
    printing_count = request.form.get('printingCount', type=int)  # Get printing count from request

    if file.filename == '':
        return 'No file selected'

    if file.filename[-4:] != '.bmp':
        return 'Selected file was not in .bmp type'

    filename = file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Store printing count data in MongoDB
    document = {
        'filename': filename,
        'printing_count': printing_count,
        'file_path': file_path
    }
    # collection.insert_one(document)

    return (f'File {filename} successfully received and saved to ArmBoard with printing count of {printing_count}')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
