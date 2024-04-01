#!/bin/bash
# This script should be used to format images for a fresh labeling run.
# This will remove any existing txt files in this folder.

folder_path="./static/target"

# Navigate to the folder containing the images
cd "$folder_path" || exit

# Remove any existing text files
rm *.txt

# Initialize counter
count=1

# Loop through each image file in the folder
for file in *.{webp,WEBP,jpg,JPG,jpeg,JPEG,png,PNG}; do
    # Check if the file is a regular file
    if [ -f "$file" ]; then
        # Convert the webp images to PNG if applicable
        if [[ "$file" == *.{webp,WEBP} ]]; then
            convert "$file" "${file%.*}.png"
            rm "$file"
        fi

        # Get the dimensions of the image
        dimensions=$(identify -format "%wx%h" "$file")
        # Extract width and height from dimensions
        width=$(echo "$dimensions" | cut -d'x' -f1)
        height=$(echo "$dimensions" | cut -d'x' -f2)

        # Check if the largest dimension is greater than or equal to 2500
        if [ "$width" -ge 2500 ] || [ "$height" -ge 2500 ]; then
            # Resize the image while preserving aspect ratio
            convert "$file" -auto-orient -resize 2500x2500\> "$file"
        fi

        # Rename the image file to .png format with sequential numbering
        mv "$file" "$count.png"
        touch "$count.txt"
        
        # Increment counter
        ((count++))
    fi
done

