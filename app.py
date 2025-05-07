from flask import Flask, render_template, request, jsonify
import os
import shutil

app = Flask(__name__)

TARGET_BASE = './static/target/'
COMPLETED_BASE = './static/completed/'

@app.route('/')
def index():
    # List subdirectories in target folder for selection
    subdirs = [name for name in os.listdir(TARGET_BASE) if os.path.isdir(os.path.join(TARGET_BASE, name))]
    return render_template('index.html', subdirs=subdirs)

@app.route('/get_media/<subdir>')
def get_media(subdir):
    target_folder = os.path.join(TARGET_BASE, subdir)
    all_files = os.listdir(target_folder)
    media_files = []

    for f in all_files:
        if f.endswith(('.jpg', '.png', '.jpeg', '.mp4')):
            media_files.append(target_folder + '/' + f)

    # Sort based on numeric prefix
    def get_sort_index(filename):
        basename = os.path.basename(filename)
        number_part = basename.split('.')[0]
        try:
            return int(number_part)
        except:
            return 0

    media_files = sorted(media_files, key=get_sort_index)

    # Load captions
    caption_files = []
    for f in all_files:
        if f.endswith('.txt'):
            caption_files.append(os.path.join(target_folder, f))
    captions = []

    for cap_path in caption_files:
        with open(cap_path) as f:
            captions.append(f.readline().strip())

    return jsonify({'media_files': media_files, 'captions': captions})

@app.route('/move_media', methods=['POST'])
def move_media():
    data = request.get_json()
    try:
        # Move media file
        shutil.move(data["srcPathMedia"], data["dstPathMedia"])
        # Move caption file
        shutil.move(data["srcPathCap"], data["dstPathCap"])

        # Save caption
        with open(data["dstPathCap"], "w") as f:
            f.write(data["caption"])

        # Save notes
        with open("./notes.txt", "a") as f:
            f.write(f"{data['dstPathMedia']} : {data['notes']}\n")

        return jsonify({'message': 'Media moved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
