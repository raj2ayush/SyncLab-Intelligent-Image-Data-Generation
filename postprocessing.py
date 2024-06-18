import os
import imgaug.augmenters as iaa
import numpy as np
from PIL import Image

def postProcessing():
    # Set the path to the directory containing the images
    dir_path = "data/happy human face"

    if not os.path.exists('augmented_images'):
        os.makedirs('augmented_images')

    # Define the new height and width of the image after scaling
    #Take input from user
    new_height = 450
    new_width = 450

    # Define the augmentations to be performed
    seq = iaa.Sequential([
        # iaa.Flipud(),  # vertically flip the image
        iaa.Affine(rotate=(-179, 179)),  # rotate the image by a random angle between -10 and 10 degrees
        iaa.GaussianBlur(sigma=(0, 1.0)),  # apply gaussian blur with a random sigma between 0 and 1.0
        iaa.Resize({"height": new_height, "width": new_width})  # resize the image to height and width of 300 pixels
    ])

    # Define the number of augmented images to generate
    num_aug_images = 10

    # Get the list of files in the directory
    file_list = os.listdir(dir_path)

    # Count the number of image files in the directory
    num_images = sum([1 for file in file_list if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png")])

    # Loop over each image file in the directory and generate the augmented images
    for file in file_list:
        # Check if the file is an image file
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            # Set the path to the image file
            image_file = os.path.join(dir_path, file)

            # Open the image file
            img = Image.open(image_file)

            # Resize the image to the desired dimensions
            img = img.resize((new_width, new_height))

            # Convert the image to a numpy array
            img_array = np.array(img)

            # Generate the augmented images
            for i in range(num_aug_images):
                # Apply the augmentations to the image array with random values
                aug_img_array = seq.augment_image(img_array)

                # Convert the augmented image back to PIL Image format
                aug_img = Image.fromarray(aug_img_array)

                # Get the original file name and remove the file extension
                file_name, file_extension = os.path.splitext(file)

                # Set the new file type you want to convert the image to
                new_file_type = "jpg"

                # Create a new file name with the new file extension and a suffix for the augmented image
                new_file_name = file_name + "_aug_" + str(i) + "." + new_file_type
                aug_img.save(os.path.join('augmented_images', new_file_name))

                # Save the augmented image in the local directory
                # aug_img.save(os.path.join(dir_path, new_file_name))
    print("Augmented images generated for", num_images, "images.")

