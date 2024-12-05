# Alex Nagy TOTALLY wrote this script and for sure wasn't chatGPT..
import os
from flask import Flask, request, jsonify
from google.cloud import storage


app = Flask(__name__)

# Google Cloud Storage bucket name
BUCKET_NAME = "mdxbikesdotnet"  # Replace with your bucket name

# Max file size limit (2GB)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 * 1024  # 2GB file limit

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save file to Google Cloud Storage
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(file.filename)
    
    try:
        # Upload file to the bucket
        blob.upload_from_file(file)
        return jsonify({
            'message': 'File uploaded successfully',
            'fileUrl': blob.public_url
        })
    except Exception as e:
        return jsonify({'error': f'Error uploading file: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

