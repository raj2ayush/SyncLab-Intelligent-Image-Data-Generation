import os

def check_and_delete_image(source_dir, target_dir, image_file):
    source_path = os.path.join(source_dir, image_file)
    target_path = os.path.join(target_dir, image_file)

    if os.path.exists(target_path):
        print(f"Image {image_file} found in both directories.")
    else:
        print(f"Image {image_file} not found in the target directory. Deleting from the source directory.")
        os.remove(source_path)

# Specify the directories
source_directory = 'inference_images'
target_directory = 'yolov5/runs/detect/inference_17'

# List all image files in the source directory
source_files = os.listdir(source_directory)

# Check each image file
for image_file in source_files:
    if image_file.endswith('.jpg') or image_file.endswith('.png') or image_file.endswith('.jpeg'):  # Specify the image file extensions you want to check
        check_and_delete_image(source_directory, target_directory, image_file)
