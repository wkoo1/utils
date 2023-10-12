from operator import index
import numpy as np
import os
import cv2
import shutil
from PIL import Image
import SimpleITK as sitk

def searchDirFile(rootDir,saveDir):
    for dir_or_file in os.listdir(rootDir):
        try:
            filePath = os.path.join(rootDir, dir_or_file)
            # 判断是否为文件
            if os.path.isfile(filePath):
                # 如果是文件再判断是否以.jpg结尾，不是则跳过本次循环
                if os.path.basename(filePath).endswith('.nii.gz'):
                    print('imgBox fileName is: '+os.path.basename(filePath))
                    itk_img = sitk.ReadImage(filePath)
                    img_array = sitk.GetArrayFromImage(itk_img)
                    # frame_num, width, height = img_array.shape
                    path = f'{saveDir}'
                    # index = -1
                    # for img_item in img_array:
                    #     index = index + 1
                    #     filename = os.path.splitext(os.path.basename(filePath))[0]# + ".jpg"
                    #     filename = filename.split('.')[0] + '.jpg'
                    #     filename = os.path.join(path, filename)
                    #     print('filename is: '+filename)
                    #     cv2.imwrite(filename, img_item)
                        #cv2.imwrite("%s/%d.png" % (path, index), img_item)
                    if not os.path.exists(path):
                        os.makedirs(path)

                    filename = os.path.splitext(os.path.basename(filePath))[0]# + ".jpg"
                    filename = filename.split('.')[0] + '.png'
                    filename = os.path.join(path, filename)
                    print('filename is: '+filename)
                    cv2.imwrite(filename, img_array)
 
                else:
                    continue
            # 如果是个dir，则再次调用此函数，传入当前目录，递归处理。
            elif os.path.isdir(filePath):
                searchDirFile(filePath, saveDir)
            else: print('not file and dir '+os.path.basename(filePath))
        except:
            continue
 
 
 
if __name__ == '__main__':
    rootDir = 'D:/oukai/dataset/Camus/0label_ES'
    saveDir = 'D:/oukai/dataset/Camus/label_ES_png'
    searchDirFile(rootDir, saveDir)
    print("the end !!!")
