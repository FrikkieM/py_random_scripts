# Script used to create PDF files from subfolders containing PNG files
# The source PNG files are all the same size

import os
from PIL import Image

def images_to_pdf_in_subdirectories(base_directory):
    for root, dirs, files in os.walk(base_directory):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            # List all PNG files and sort them numerically
            png_files = sorted(
                [f for f in os.listdir(dir_path) if f.endswith('.png')],
                key=lambda x: int(os.path.splitext(x)[0])
            )
            
            if not png_files:
                continue

            # Full paths of the sorted PNG files
            png_files = [os.path.join(dir_path, f) for f in png_files]

            # Open images and convert to RGB (required for saving as PDF)
            images = [Image.open(png).convert('RGB') for png in png_files]

            # Save images as a single PDF file
            pdf_path = os.path.join(dir_path, f"{dir_name}.pdf")
            images[0].save(pdf_path, save_all=True, append_images=images[1:])
            print(f"Created PDF: {pdf_path}")

# Get the current directory
current_directory = os.getcwd()

# Call the function
images_to_pdf_in_subdirectories(current_directory)
