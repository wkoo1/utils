#--------------------------------------------------------#
#   该文件用于调整标签的格式
#-------------------------------------------------------#
import os

import numpy as np
from PIL import Image
from tqdm import tqdm

#-----------------------------------------------------------------------------------#
#   Origin_SegmentationClass_path   原始标签所在的路径
#   Out_SegmentationClass_path      输出标签所在的路径
#                                   处理后的标签为灰度图，如果设置的值太小会看不见具体情况。
#-----------------------------------------------------------------------------------#
# Origin_SegmentationClass_path   = "D:\\oukai\\dataset\\nyuv2\\labels40"
Out_SegmentationClass_path      = "D:\\oukai\\dataset\\cityscapes\\gtFine\\trainval_labels19_nobackground"

# 定义文本文件路径
txt_file_path = "D:\\oukai\\dataset\\SUNRGBD\\test_label_png.txt"

# 从文本文件中读取路径
with open(txt_file_path, 'r') as file:
    paths = file.readlines()

# 去除每个路径的换行符
Origin_SegmentationClass_path = [path.strip() for path in paths]

#-----------------------------------------------------------------------------------#
#   Origin_Point_Value  原始标签对应的像素点值
#   Out_Point_Value     输出标签对应的像素点值
#                       Origin_Point_Value需要与Out_Point_Value一一对应。
#   举例如下，当：
#   Origin_Point_Value = np.array([0, 255])；Out_Point_Value = np.array([0, 1])
#   代表将原始标签中值为0的像素点，调整为0，将原始标签中值为255的像素点，调整为1。
#
#   示例中仅调整了两个像素点值，实际上可以更多个，如：
#   Origin_Point_Value = np.array([0, 128, 255])；Out_Point_Value = np.array([0, 1, 2])
#
#   也可以是数组（当标签值为RGB像素点时），如
#   Origin_Point_Value = np.array([[0, 0, 0], [1, 1, 1]])；Out_Point_Value = np.array([0, 1])
#-----------------------------------------------------------------------------------#
# cityscapes dataset
Origin_Point_Value              = np.array([0  ,1  ,2  ,3  ,4  ,5  ,6  ,7,8,9  ,10 ,11,12,13, 14 , 15 , 17 ,18 ,19,20,21,22,23,24,25,26,27,28,29 , 30 , 31,32,33])
Out_Point_Value                 = np.array([255,255,255,255,255,255,255,0,1,255,255, 2, 3, 4, 255, 255, 5, 255, 6, 7, 8, 9,10,11,12,13,14,15,255, 255, 16,17,18])

# Origin_Point_Value              = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
# Out_Point_Value                 = np.array([0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

if __name__ == "__main__":
    # if not os.path.exists(Out_SegmentationClass_path):
    #     os.makedirs(Out_SegmentationClass_path)

    #---------------------------#
    #   遍历标签并赋值
    #---------------------------#
    # png_names = os.listdir(Origin_SegmentationClass_path)
    # print("正在遍历全部标签。")
    # for png_name in tqdm(png_names):
    #     png     = Image.open(os.path.join(Origin_SegmentationClass_path, png_name))
    #     w, h    = png.size
        
    #     png     = np.array(png)
    #     out_png = np.zeros([h, w])
    #     for i in range(len(Origin_Point_Value)):
    #         mask = png[:, :] == Origin_Point_Value[i]
    #         if len(np.shape(mask)) > 2:
    #             mask = mask.all(-1)
    #         out_png[mask] = Out_Point_Value[i]
        
    #     out_png = Image.fromarray(np.array(out_png, np.uint8))
    #     out_png.save(os.path.join(Out_SegmentationClass_path, png_name))
    #-------------------------------------#
    #   统计输出，各个像素点的值得个数
    #-------------------------------------#
    print("正在统计输出的图片每个像素点的数量。")
    classes_nums        = np.zeros([256], np.int)
    for png_name in tqdm(Origin_SegmentationClass_path):
        png_file_name   = os.path.join("D:\\oukai\\dataset\\SUNRGBD\\", png_name +".png")
        if not os.path.exists(png_file_name):
            raise ValueError("未检测到标签图片%s，请查看具体路径下文件是否存在以及后缀是否为png。"%(png_file_name))
        
        png             = np.array(Image.open(png_file_name), np.uint8)
        classes_nums    += np.bincount(np.reshape(png, [-1]), minlength=256)
        
    print("打印像素点的值与数量。")
    print('-' * 37)
    print("| %15s | %15s |"%("Key", "Value"))
    print('-' * 37)
    for i in range(256):
        if classes_nums[i] > 0:
            print("| %15s | %15s |"%(str(i), str(classes_nums[i])))
            print('-' * 37)