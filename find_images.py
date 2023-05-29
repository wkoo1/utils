from operator import index
import numpy as np
import os
import cv2
import shutil
from PIL import Image
import SimpleITK as sitk

def searchDirFile(rootDir, saveDir):
    for dir_or_file in os.listdir(rootDir):
        try:
            filePath = os.path.join(rootDir, dir_or_file)
            # 判断是否为文件
            if os.path.isfile(filePath):
                # 如果是文件再判断是否以.jpg结尾，是则将其额外保存
                if os.path.basename(filePath).endswith('.jpg'):
                    print('imgBox fileName is: '+os.path.basename(filePath))
                    img_array = cv2.imread(filePath)
                    filename = os.path.splitext(os.path.basename(filePath))[0] + ".jpg"
                    filename = os.path.join(saveDir, filename)
                    print('filename is: '+filename)
                    cv2.imwrite(filename, img_array)
            # 如果是个dir，则递归调用此函数，传入当前目录。
            elif os.path.isdir(filePath):
                searchDirFile(filePath, saveDir)
        except:
            continue

if __name__ == '__main__':
    rootDir = 'D:/oukai/dataset/ADE20K/images/ADE/validation'
    saveDir = 'D:/oukai/dataset/ADE20K/val/images'
    searchDirFile(rootDir, saveDir)
    print("the end !!!")
