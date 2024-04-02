#!/bin/bash

# Set the directory path
directory="./static/completed"

# Get the list of .png and .txt files without extensions
png_files=$(find "$directory" -type f -name "*.png" | sed 's/\.png$//')
txt_files=$(find "$directory" -type f -name "*.txt" | sed 's/\.txt$//')

# Find files without mates
orphan_files=$(comm -3 <(echo "$png_files" | sort) <(echo "$txt_files" | sort))

# Print the files without mates
echo "$orphan_files"
