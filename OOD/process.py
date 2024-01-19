import os
from PIL import Image, ImageFilter

def scale_image(file_path, output_folder, scale_factor=0.7):
    with Image.open(file_path) as img:
        # Calculate the new size, scaling down by 30%
        new_size = tuple([int(scale_factor * dim) for dim in img.size])
        
        # Resize the image using the BICUBIC resampling filter
        scaled_img = img.resize(new_size, Image.Resampling.BICUBIC)

        # Optionally apply a sharpening filter
        sharpened_img = scaled_img.filter(ImageFilter.SHARPEN)

        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Save the sharpened image in the output folder
        output_file_path = os.path.join(output_folder, os.path.basename(file_path))
        sharpened_img.save(output_file_path)

def process_images_in_current_folder():
    current_folder = os.getcwd()
    output_folder = os.path.join(current_folder, 'scaled_images')

    for filename in os.listdir(current_folder):
        if filename.lower().endswith('.png'):
            file_path = os.path.join(current_folder, filename)
            scale_image(file_path, output_folder)

process_images_in_current_folder()
