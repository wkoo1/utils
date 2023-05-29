import os

# 文件夹路径
folder_path = 'D:/oukai/dataset/ADE20K/train/images'

# 保存txt文件路径
txt_file_path = 'D:/oukai/dataset/ADE20K/train_jpg.txt'

# 获取文件夹内所有图像文件的文件名
image_names = [file for file in os.listdir(folder_path) if file.endswith(('.jpg', '.png', '.jpeg'))]

# 将图像文件名保存到txt文件
with open(txt_file_path, 'w') as file:
    for image_name in image_names:
        file.write(image_name + '\n')
