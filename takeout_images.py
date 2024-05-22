import os
import shutil

def read_txt_file(file_path):
    """
    Read the txt file and return a list of image filenames.
    """
    with open(file_path, 'r') as file:
        image_filenames = file.read().splitlines()
    return image_filenames

def move_images(image_filenames, source_dir, destination_dir):
    """
    Move images from source directory to destination directory based on the list of filenames.
    
    Args:
    - image_filenames (list): List of image filenames to be moved.
    - source_dir (str): Directory containing the original images.
    - destination_dir (str): Directory to move the images to.
    """
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for image_name in image_filenames:
        source_path = os.path.join(source_dir, image_name + '.png')
        destination_path = os.path.join(destination_dir, image_name + '.png')

        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
            print(f"Moved {image_name + '.png'} to {destination_path}")
        else:
            print(f"Image {image_name + '.png'} does not exist in the source directory.")

# Example usage:
txt_file_path = 'D:/oukai/dataset/cityscapes/gtFine/val_labels.txt'
source_directory = 'Z:/x/Meta_learning/data/cityscapes/trainval_labels9'
destination_directory = 'Z:/x/Meta_learning/data/cityscapes/val_labels9'

image_filenames = read_txt_file(txt_file_path)
move_images(image_filenames, source_directory, destination_directory)
