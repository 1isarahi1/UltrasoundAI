import zipfile
import os

# Define the path to your zip file and the extraction directory
zip_file_path = '/Users/sarahabellard/Documents/MAIShacks/FETAL_PLANES_ZENODO.zip'
extraction_dir = '/Users/sarahabellard/Documents/MAIShacks/extractedimages'

# Create the extraction directory if it doesn't exist
os.makedirs(extraction_dir, exist_ok=True)

# Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_dir)
