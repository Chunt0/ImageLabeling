#!/bin/bash

folder_path="./static/target"

# Navigate to the folder containing the images
cd "$folder_path" || exit

# Counter for renaming files
count=1

# Loop through each image file in the folder
for file in *.{webp, WEBP}; do
    # Check if the file is a regular file and ends with ".webp"
    if [ -f "$image_file" ] && [[ "$image_file" == *.webp ]]; then
        # Get the filename without extension
        filename_no_ext="${image_file%.*}"
        # Convert the webp image to PNG
        convert "$image_file" "${filename_no_ext}.png"
        # Remove the original webp file
        rm "$image_file"
    fi
done

# Loop through each image file in the folder
for file in *.{jpg,JPG,jpeg,JPEG,png,PNG}; do
    # Check if the file is a regular file
    if [ -f "$file" ]; then
        # Rename the image file to .png format
        mv "$file" "$count.png"
        # Create a corresponding text file with the same name
        touch "$count.txt"
        # Increment the counter
        ((count++))
    fi
done

