from flask import Flask, render_template, request, jsonify
import os
import shutil
import csv

app = Flask(__name__)

@app.route('/')
def index():
    # List image files in the 'img' folder (update the folder path if needed)
    image_folder = './static/img/target/'
    image_files = [image_folder+f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

    return render_template('index.html', image_files=image_files)

@app.route('/build_imagefolder', methods=['POST'])
def build_imagefolder():
    data = request.get_json()
    metadata = []
    print(data)
    for d in data:
        image_path = d['dstPath'].split('/')[-1]
        shutil.copy2(d['srcPath'],d['dstPath'])
        metadata.append((image_path, d['caption']))
    
    with open("./static/img/completed/metadata.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(metadata)
    
    return "Metadata received successfully!"

if __name__ == '__main__':
    app.run(debug=True)
