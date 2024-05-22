# e.g. 数据集中有9个类别，标签分别是[1,2,3,4,5,6,7,8,9,255],当图像拥有像素点值1或2或3的时候，将图像额外保存下来。

import os
from PIL import Image
import numpy as np
from tqdm import tqdm

def load_image(image_path):
    """
    Load an image from a file path and return it as a numpy array.
    """
    return np.array(Image.open(image_path))

def save_image(image, save_path):
    """
    Save a numpy array as an image to the specified file path.
    """
    Image.fromarray(image).save(save_path)

def process_image_dataset(input_dir, output_dir, labels_to_check=[7, 8, 9]):
    """
    Process an image dataset by checking if images contain certain labels and saving them if they do.

    Args:
    - input_dir (str): Directory containing the input images.
    - output_dir (str): Directory to save the filtered images.
    - labels_to_check (list): List of labels to check for in the images.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for image_name in tqdm(os.listdir(input_dir)):
        image_path = os.path.join(input_dir, image_name)
        
        if os.path.isfile(image_path):
            image = load_image(image_path)
            
            # Check if any pixel in the image has a value in labels_to_check
            if np.any(np.isin(image, labels_to_check)):
                save_path = os.path.join(output_dir, image_name)
                save_image(image, save_path)
                # print(f"Image {image_name} saved to {save_path}")

# Example usage:
input_directory = "Z:\\x\\Meta_learning\\data\\Cityscapes\\val_labels9"
output_directory = "Z:\\x\\Meta_learning\\data\\Cityscapes\\val_labels9_split2"

process_image_dataset(input_directory, output_directory)
