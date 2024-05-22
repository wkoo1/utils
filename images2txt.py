import os
from tqdm import tqdm

# 文件夹路径
jpg_folder_path = 'Z:/x/Meta_learning/data/cityscapes/val_labels9_split0'
mask_folder_path = 'Z:/x/Meta_learning/data/cityscapes/val_labels9_split0'

# 保存txt文件路径
txt_file_path = 'Z:/x/Meta_learning/data/cityscapes/val_labels9_split0.txt'

# # 获取文件夹内所有图像文件的文件名
# image_names = [file for file in os.listdir(jpg_folder_path) if file.endswith(('.jpg', '.png', '.jpeg'))]
# mask_names = [file for file in os.listdir(mask_folder_path) if file.endswith(('.png'))]

# # 将图像文件名保存到txt文件
# with open(txt_file_path, 'w') as file:
#     for image_name in image_names:
#         file.write(image_name + '\n')

# 获取文件夹内所有图像文件的文件名
image_names = sorted([file for file in os.listdir(jpg_folder_path) if file.endswith(('.jpg', '.png', '.jpeg'))])
mask_names = sorted([file for file in os.listdir(mask_folder_path) if file.endswith(('.png'))])

# 确保图像和掩码的数量相同
assert len(image_names) == len(mask_names), "The number of images and masks should be the same."

# 将图像文件名和掩码文件名保存到txt文件
with open(txt_file_path, 'w') as file:
    for image_name, mask_name in zip(image_names, mask_names):
        file.write('../data/cityscapes/trainval_jpg/' + image_name + ' ' + '../data/cityscapes/trainval_labels9/' + mask_name + '\n')


# path = 'D:/oukai/dataset/SUNRGBD/'
# depth_list_path = 'D:/oukai/dataset/SUNRGBD/val_depth_noimages.txt'
# txt_file_path = 'D:/oukai/dataset/SUNRGBD/val_depth_images.txt'

# # 遍历txt文件中的所有文件路径
# with open(depth_list_path, 'r') as f:
#     depth_files = [line.strip() for line in f.readlines()]

# for depth_file in tqdm(depth_files):
#     image_dir = os.path.dirname(depth_file)
#     image_names = [os.path.join(image_dir, file) for file in os.listdir(os.path.join(path, image_dir)) if file.endswith(('.jpg', '.png', '.jpeg'))]
#     with open(txt_file_path, 'a') as file:
#         file.write('\n'.join(image_names) + '\n')