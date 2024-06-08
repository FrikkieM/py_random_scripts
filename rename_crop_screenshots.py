# Script used to cleanup screenshots in a folder by renaming them in order and cropping them


import os
from PIL import Image
from datetime import datetime

# Function to get the creation date of a file
def get_creation_date(file_path):
    return os.path.getctime(file_path)

# Function to rename and crop images
def rename_and_crop_images(directory):
    # List all PNG files in the directory
    files = [f for f in os.listdir(directory) if f.endswith('.png')]
    
    # Sort files by creation date
    files.sort(key=lambda x: get_creation_date(os.path.join(directory, x)))

    # Process each file
    for index, file_name in enumerate(files, start=1):
        old_file_path = os.path.join(directory, file_name)
        new_file_name = f"{index}.png"
        new_file_path = os.path.join(directory, new_file_name)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        
        # Open the image
        with Image.open(new_file_path) as img:
            # Calculate cropping box (left, upper, right, lower)
            left = 311
            top = 83
            right = img.width - 311
            bottom = img.height - 83
            cropped_img = img.crop((left, top, right, bottom))
            
            # Save the cropped image, overwriting the existing file
            cropped_img.save(new_file_path)

# Get the current directory
current_directory = os.getcwd()

# Call the function
rename_and_crop_images(current_directory)
