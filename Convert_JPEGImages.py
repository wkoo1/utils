#--------------------------------------------------------#
#   该文件用于调整输入彩色图片的后缀
#-------------------------------------------------------#
import os

import numpy as np
from PIL import Image
from tqdm import tqdm

#--------------------------------------------------------#
#   Origin_JPEGImages_path   原始标签所在的路径
#   Out_JPEGImages_path      输出标签所在的路径
#--------------------------------------------------------#

# JPG---->PNG

# Origin_JPEGImages_path   = "D:\\oukai\\dataset\\cityscapes\\leftImg8bit\\test_all"
# Out_JPEGImages_path      = "D:\\oukai\\dataset\\cityscapes\\leftImg8bit\\test_jpg"

# if __name__ == "__main__":
#     if not os.path.exists(Out_JPEGImages_path):
#         os.makedirs(Out_JPEGImages_path)

#     #---------------------------#
#     #   遍历标签并赋值
#     #---------------------------#
#     image_names = os.listdir(Origin_JPEGImages_path)
#     print("正在遍历全部图片。")
#     for image_name in tqdm(image_names):
#         image   = Image.open(os.path.join(Origin_JPEGImages_path, image_name))
#         image   = image.convert('RGB')
#         image.save(os.path.join(Out_JPEGImages_path, os.path.splitext(image_name)[0] + '.jpg'))



#24bit---->8bit
Origin_JPEGImages_path   = "D:\\oukai\\dataset\\ADE20K\\val\\labels"
Out_JPEGImages_path      = "D:\\oukai\\dataset\\ADE20K\\val\\labels2"

if __name__ == "__main__":
    if not os.path.exists(Out_JPEGImages_path):
        os.makedirs(Out_JPEGImages_path)

    #---------------------------#
    #   遍历标签并赋值
    #---------------------------#
    image_names = os.listdir(Origin_JPEGImages_path)
    print("正在遍历全部图片。")
    for image_name in tqdm(image_names):
        image   = Image.open(os.path.join(Origin_JPEGImages_path, image_name))
        image   = image.convert('L')
        image.save(os.path.join(Out_JPEGImages_path, os.path.splitext(image_name)[0] + '.png'))

