from PIL import Image
import os

folder_path = './old/'  # Replace with your folder path
new_path = './static/target/'

blip_caption = False # Keep this false unless you plan to do BLIP captioning on dataset
count = 0
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg', '.webp', '.png')):
        count += 1
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        new_filename = f'{count}.png'
        img.save(os.path.join(new_path, new_filename))
        
        if not blip_caption:
            with open(f"{new_path}{count}.txt", "w") as f:
                f.write("")
        
