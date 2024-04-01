#!/bin/bash

# Define the folder path containing the images
folder_path="./static/target"

# Loop through each image file in the folder
for image_file in "$folder_path"/*; do
    # Check if the file is a regular file and ends with ".png"
    if [ -f "$image_file" ] && [[ "$image_file" == *.png ]]; then
        # Get the dimensions of the image
        dimensions=$(identify -format "%wx%h" "$image_file")
        # Extract width and height from dimensions
        width=$(echo "$dimensions" | cut -d'x' -f1)
        height=$(echo "$dimensions" | cut -d'x' -f2)
        # Check if the largest dimension is greater than or equal to 2500
        if [ "$width" -ge 2500 ] || [ "$height" -ge 2500 ]; then
            # Resize the image to fit within 3000x3000 while preserving aspect ratio
            convert "$image_file" -auto-orient -resize 61%x61% "$image_file"
        fi
    fi
done

