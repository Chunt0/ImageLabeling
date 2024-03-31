#!/bin/bash

# Define the folder path containing the images
folder_path="./static/target"
destination_folder="./static/smalls"

mkdir -p "$destination_folder"

# Loop through each image file in the folder
for image_file in "$folder_path"/*; do
    # Check if the file is a regular file
    if [ -f "$image_file" ]; then
        dimensions=$(identify -format "%wx%h" "$image_file")
        # Extract width and height from dimensions
        width=$(echo "$dimensions" | cut -d'x' -f1)
        height=$(echo "$dimensions" | cut -d'x' -f2)
        if [ "$width" -le 400 ] || [ "$height" -le 400 ]; then
            # Resize the image to fit within 3000x3000 while preserving aspect ratio
            rm -f "$image_file"
        fi
        if [ "$width" -le 700 ] || [ "$height" -le 700 ]; then
            mv "$image_file" "$destination_folder"
        fi
    fi
done


