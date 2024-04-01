#!/bin/bash
# This script should be used to format images for a fresh labeling run.
# This will remove any existing txt files in this folder.

folder_path="./static/target"

# Navigate to the folder containing the images
cd "$folder_path" || exit


# Loop through each image file in the folder
for file in *.{webp, WEBP}; do
    # Check if the file is a regular file and ends with ".webp"
    if [ -f "$file" ]; then
        # Convert the webp image to PNG
        convert "$file" "${file%.*}.png"
        # Remove the original webp file
        rm "$file"
    fi
done

# Remove any txt files
for file in *.{txt}; do
    rm "$file"
done

# Loop through each image file in the folder
for file in *.{jpg,JPG,jpeg,JPEG,png,PNG}; do
        # Check if the file is a regular file and ends with ".png"
    if [ -f "$file" ]; then
        # Get the dimensions of the image
        dimensions=$(identify -format "%wx%h" "$image_file")
        # Extract width and height from dimensions
        width=$(echo "$dimensions" | cut -d'x' -f1)
        height=$(echo "$dimensions" | cut -d'x' -f2)
        
        ############################################
        ##############CRITICAL######################
        # Check if the largest dimension is greater than or equal to some cutoff value -> i.e. 2500
        if [ "$width" -ge 2500 ] || [ "$height" -ge 2500 ]; then
            ############################################
            ##############CRITICAL######################
            # Resize the image to fit the desired ratio! (i.e. 50%x50%) 
            convert "$file" -auto-orient -resize 61%x61% "$file"
        fi
        
        # Counter for renaming files
        count=1
        # Rename the image file to .png format
        mv "$file" "$count.png"
        # Create a corresponding text file with the same name
        touch "$count.txt"
        # Increment the counter
        ((count++))
    fi
done

