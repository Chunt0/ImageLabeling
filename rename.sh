#!/bin/bash

# Ensure the user has provided the folder path
if [ $# -ne 1 ]; then
    echo "Usage: $0 folder_path"
    exit 1
fi

# Navigate to the folder containing the images
cd "$1" || exit

# Counter for renaming files
count=1

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

