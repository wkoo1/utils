import os
from tqdm import tqdm

# # 文件夹路径
# folder_path = 'D:/oukai/dataset/ADE20K/train/images'

# # 保存txt文件路径
# txt_file_path = 'D:/oukai/dataset/ADE20K/train_jpg.txt'

# # 获取文件夹内所有图像文件的文件名
# image_names = [file for file in os.listdir(folder_path) if file.endswith(('.jpg', '.png', '.jpeg'))]

# # 将图像文件名保存到txt文件
# with open(txt_file_path, 'w') as file:
#     for image_name in image_names:
#         file.write(image_name + '\n')


path = 'D:/oukai/dataset/SUNRGBD/'
depth_list_path = 'D:/oukai/dataset/SUNRGBD/val_depth_noimages.txt'
txt_file_path = 'D:/oukai/dataset/SUNRGBD/val_depth_images.txt'

# 遍历txt文件中的所有文件路径
with open(depth_list_path, 'r') as f:
    depth_files = [line.strip() for line in f.readlines()]

for depth_file in tqdm(depth_files):
    image_dir = os.path.dirname(depth_file)
    image_names = [os.path.join(image_dir, file) for file in os.listdir(os.path.join(path, image_dir)) if file.endswith(('.jpg', '.png', '.jpeg'))]
    with open(txt_file_path, 'a') as file:
        file.write('\n'.join(image_names) + '\n')