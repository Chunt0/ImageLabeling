from flask import Flask, render_template, request, jsonify
import os
import shutil
import csv

app = Flask(__name__)

@app.route('/')
def index():
    # When the page is loaded
    # List image files in the 'img' folder (update the folder path if needed)
    image_folder = './static/target/'
    def sort_key(x): return int(x.split('/')[-1].split('.')[0])
    image_files = [image_folder+f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
    image_files = sorted(image_files, key=sort_key)
    caption_files = [image_folder+f for f in os.listdir(image_folder)if f.endswith(".txt")]
    caption_files = sorted(caption_files, key=sort_key)
    captions = []
    for caption_path in caption_files:
        with open(caption_path) as f:
            captions.append(f.readline().strip())
    return render_template('index.html', image_files=image_files, caption_files=caption_files, captions=captions)

@app.route('/move_image', methods=['POST'])
def move_image():
    data = request.get_json()
    shutil.move(data["srcPathImg"], data["dstPathImg"])
    shutil.move(data["srcPathCap"], data["dstPathCap"])
    with open(data["dstPathCap"], "w") as f:
        f.write(data["caption"])
    with open("./notes.txt", "a") as f:
        f.write(f"{data['dstPathImg']} : {data['notes']}\n")
    try:
        # Logic to handle moving the image
        return jsonify({'message': 'Image moved successfully'}), 200  # HTTP 200 OK
    except Exception as e:
        # Handle exception and return an error response
        return jsonify({'error': str(e)}), 500  # HTTP 500 Internal Server Error
 

if __name__ == '__main__':
    app.run(debug=True)
