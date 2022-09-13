# import cv2
# import SimpleITK as sitk
# import matplotlib.pyplot as plt
# import numpy as np
# filename = 'D:/oukai/dataset/Camus/training/patient0001/patient0001_2CH_ED.mhd'
# itk_img = sitk.ReadImage(filename)
# img_array = sitk.GetArrayFromImage(itk_img)
# print(img_array.shape)


# import SimpleITK as sitk
# import os
# import cv2
# filename = 'D:/oukai/dataset/Camus/training/patient0001/patient0001_2CH_ED.mhd'
# path = 'D:/oukai/dataset/Camus'   #存放拆分得到图像的路径
# itk_img = sitk.ReadImage(filename)
# img_array = sitk.GetArrayFromImage(itk_img)
# for i, im in enumerate(img_array):
#   cv2.imwrite(os.path.join(path, '{}.png'.format(i)), im)

import SimpleITK as sitk
import cv2
filename = 'D:/oukai/dataset/Camus/training/patient0001/patient0001_2CH_ED.mhd'
itk_img = sitk.ReadImage(filename)
img_array = sitk.GetArrayFromImage(itk_img)
frame_num, width, height = img_array.shape
path = 'D:/oukai/dataset/Camus'   #存放拆分得到图像的路径
index = -1
for img_item in img_array:
    index = index + 1
    cv2.imwrite("%s/%d.png" % (path, index), img_item)
print("done!")
