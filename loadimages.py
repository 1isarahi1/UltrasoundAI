from PIL import Image
import numpy as np
import os
from importzipfile import extraction_dir

# List all image file paths in the extraction directory with common image file extensions
valid_image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
image_paths = [os.path.join(extraction_dir, filename) for filename in os.listdir(extraction_dir) if any(filename.endswith(ext) for ext in valid_image_extensions)]

# Initialize empty lists for images and labels (if you have labels)
images = []
labels = []

# Loop through image paths and load images
for image_path in image_paths:
    # Load the image using Pillow
    image = Image.open(image_path)
    
    # Convert the image to a NumPy array
    image_array = np.array(image)
    
    # Append the image to the list of images
    images.append(image_array)

# Convert the list of images to a NumPy array
images = np.array(images)

# Now you can proceed with your image processing and machine learning tasks
