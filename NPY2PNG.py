import os
import numpy as np
from PIL import Image
from tqdm import tqdm

# 指定输入文件夹路径和txt文件路径
input_folder = 'D:/oukai/dataset/SUNRGBD'
npy_list_path = 'D:/oukai/dataset/SUNRGBD/train_label.txt'

# 遍历txt文件中的所有NPY文件路径
with open(npy_list_path, 'r') as f:
    npy_files = [line.strip() for line in f.readlines()]

# 遍历所有NPY文件，将其转换为PNG格式并保存到原始路径中
for npy_file in tqdm(npy_files):
    # 构造输出PNG文件路径
    png_file = os.path.join(os.path.dirname(npy_file), os.path.basename(npy_file)[:-4] + '.png')

    # 加载NPY文件中的数据
    data = np.load(os.path.join(input_folder, npy_file))

    # 将数据缩放到0-255之间的整数
    # data = (data - data.min()) / (data.max() - data.min()) * 255
    # data = data.astype(np.uint8)
    # print(data.shape)
    # 创建PIL Image对象并保存为PNG格式
    img = Image.fromarray(data)
    img.save(os.path.join(input_folder, png_file))
    # print('save to {}'.format(os.path.join(input_folder, png_file)))
