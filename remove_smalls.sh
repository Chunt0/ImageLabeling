#!/bin/bash

# Define the folder path containing the images
folder_path="./static/target"

# Loop through each image file in the folder
for image_file in "$folder_path"/*; do
    # Check if the file is a regular file
    if [ -f "$image_file" ]; then
        # Get the dimensions of the image
        dimensions=$(identify -format "%wx%h" "$image_file")
        # Extract width and height from dimensions
        width=$(echo "$dimensions" | cut -d'x' -f1)
        height=$(echo "$dimensions" | cut -d'x' -f2)
        # Check if the largest dimension is greater than or equal to 3000
        if [ "$width" -le 400 ] || [ "$height" -le 400 ]; then
            # Resize the image to fit within 3000x3000 while preserving aspect ratio
            rm -f "$image_file"
        fi
    fi
done

