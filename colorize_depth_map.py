import cv2
import numpy as np
import matplotlib.pyplot as plt

def colorize_depth_map(depth_map):
    # 根据深度值设定伪彩色映射表
    colormap = cv2.applyColorMap((depth_map / np.max(depth_map) * 255).astype(np.uint8), cv2.COLORMAP_JET)
    # print(np.max(depth_map))
    return colormap

# 读取深度图像
depth_image = cv2.imread('Z:/x/mycode/MDEASS-Net/miou_out/detection-results-d/frankfurt_000000_008206_leftImg8bit.png', cv2.IMREAD_GRAYSCALE)
# depth_image = cv2.imread('D:/oukai/dataset/nyuv2/depths/5.png', cv2.IMREAD_GRAYSCALE)
# depth_image = cv2.imread('D:/oukai/dataset/SUNRGBD/SUNRGBD/kv2/align_kv2/2014-12-18_11-34-09_260595134347/depth_bfx/0000337.png', cv2.IMREAD_GRAYSCALE)

# 读取原图像
old_img = cv2.imread('Z:/x/dataset/cityscapes/leftImg8bit/val_jpg/frankfurt_000000_008206_leftImg8bit.jpg', cv2.IMREAD_COLOR)

# 进行染色
colorized_image = colorize_depth_map(depth_image)

# 设置混合权重（alpha值）
# alpha = 0.1

# 进行图像混合
# blended_image = cv2.addWeighted(old_img, alpha, colorized_image, 1 - alpha, 0)

# 显示结果
cv2.imshow('Colorized Depth Map', colorized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
