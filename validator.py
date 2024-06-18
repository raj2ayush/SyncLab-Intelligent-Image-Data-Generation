import os
import glob
import cv2
import subprocess
import matplotlib.pyplot as plt



def inference(RES_DIR, data_path):
    # Directory to store inference results.
    infer_dir_count = len(glob.glob('runs/detect/*'))
    print(f"Current number of inference detection directories: {infer_dir_count}")
    INFER_DIR = f"inference_{infer_dir_count+1}"
    print(INFER_DIR)
    # Inference on images.
    # !python detect.py --weights runs/train/{RES_DIR}/weights/best.pt \
    # --source {data_path} --name {INFER_DIR}
    cmd = f"python detect.py --weights runs/train/{RES_DIR}/weights/best.pt --source {data_path} --name {INFER_DIR}"
    subprocess.run(cmd, shell=True)
    return INFER_DIR

def visualize(INFER_DIR):
# Visualize inference images.
    INFER_PATH = f"runs/detect/{INFER_DIR}"
    infer_images = glob.glob(f"{INFER_PATH}/*.jpg")
    print(infer_images)

    for pred_image in infer_images:
        image = cv2.imread(pred_image)
        plt.figure(figsize=(19, 16))
        plt.imshow(image[:, :, ::-1])
        plt.axis('off')
        # plt.show()
    
    ##returns path of runs/detect/inference
    return INFER_PATH

def set_res_dir():
    TRAIN = 0
    # Directory to store results
    res_dir_count = len(glob.glob('runs/train/*'))
    print(f"Current number of result directories: {res_dir_count}")
    if TRAIN:
        RES_DIR = f"results_{res_dir_count+1}"
        print(RES_DIR)
    else:
        RES_DIR = f"results_{res_dir_count}"
    return RES_DIR


def check_and_delete_image(source_dir, target_dir, image_file):
    source_path = os.path.join(source_dir, image_file)
    target_path = os.path.join(target_dir, image_file)

    if os.path.exists(target_path):
        print(f"Image {image_file} found in both directories.")
    else:
        print(f"Image {image_file} not found in the target directory. Deleting from the source directory.")
        os.remove(source_path)


def validatee():
    # Get the current directory
    current_directory = os.getcwd()
    print("Current Directory:", current_directory)

    # Change directory
    new_directory = "yolov5"
    os.chdir(new_directory)

    # Get the updated current directory
    updated_directory = os.getcwd()
    print("Updated Directory:", updated_directory)

    RES_DIR = set_res_dir()
    IMAGE_INFER_DIR = inference(RES_DIR, '../inference_images')
    checkPath = visualize(IMAGE_INFER_DIR)

    # Specify the directories
    source_directory = '../inference_images'
    # target_directory = 'yolov5/runs/detect/inference_17'
    target_directory = checkPath

    # List all image files in the source directory
    source_files = os.listdir(source_directory)

    # Check each image file
    for image_file in source_files:
        if image_file.endswith('.jpg') or image_file.endswith('.png') or image_file.endswith('.jpeg'):  # Specify the image file extensions you want to check
            check_and_delete_image(source_directory, target_directory, image_file)

