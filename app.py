from flask import Flask, render_template, request, jsonify
import os
import shutil

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    # Route for the main page
    # It lists image files and corresponding captions from the 'img' folder
    image_folder = './static/target/'
    
    # Custom sorting function to sort files based on numerical order
    def sort_key(x): return int(x.split('/')[-1].split('.')[0])

    # List and sort image files
    image_files = [image_folder + f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
    image_files = sorted(image_files, key=sort_key)

    # List and sort caption files
    caption_files = [image_folder + f for f in os.listdir(image_folder) if f.endswith(".txt")]
    caption_files = sorted(caption_files, key=sort_key)

    # Read captions from files
    captions = []
    for caption_path in caption_files:
        with open(caption_path) as f:
            captions.append(f.readline().strip())

    # Render the index page with the lists of image and caption files
    return render_template('index.html', image_files=image_files, caption_files=caption_files, captions=captions)

@app.route('/move_image', methods=['POST'])
def move_image():
    # Route to handle the moving of images and updating captions
    data = request.get_json()
    
    # Move image and caption files to new destination
    shutil.move(data["srcPathImg"], data["dstPathImg"])
    shutil.move(data["srcPathCap"], data["dstPathCap"])

    # Overwrite the destination caption file with the new caption
    with open(data["dstPathCap"], "w") as f:
        f.write(data["caption"])

    # Append notes to a notes.txt file
    with open("./notes.txt", "a") as f:
        f.write(f"{data['dstPathImg']} : {data['notes']}\n")

    try:
        # Respond with success message if no errors
        return jsonify({'message': 'Image moved successfully'}), 200  # HTTP 200 OK
    except Exception as e:
        # Handle exception and return an error response
        return jsonify({'error': str(e)}), 500  # HTTP 500 Internal Server Error

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
