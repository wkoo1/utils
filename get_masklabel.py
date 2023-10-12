import cv2
import numpy as np

# 加载掩码图像
mask_image = cv2.imread('D:\\oukai\\dataset\\Camus\\label_ED_png\\patient0001_2CH_ED_gt.png', cv2.IMREAD_GRAYSCALE)
# 获取唯一标签值
labels = np.unique(mask_image)
# 输出标签值
print(labels)
