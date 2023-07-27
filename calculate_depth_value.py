import cv2
import numpy as np

depth_image = cv2.imread('Z:/x/dataset/nyuv2/nyu_depths/15.png', cv2.IMREAD_GRAYSCALE)
depth_image_pre = cv2.imread('Z:/x/mycode/MDEASS-Net_nyu/miou_out/detection-results-d/15.png', cv2.IMREAD_GRAYSCALE)

# depth_image = cv2.imread('Z:/x/mycode/MDEASS-Net/miou_out/detection-results-d/frankfurt_000000_000576_leftImg8bit.png', cv2.IMREAD_GRAYSCALE)
# depth_image = cv2.imread('Z:/x/dataset/cityscapes/disparity/trainval_depth/frankfurt_000000_000576_disparity.png', cv2.IMREAD_GRAYSCALE)

de = depth_image.astype(np.float32) /255.0
de_pre = depth_image_pre.astype(np.float32) /255.0

demax  = np.max(de)
demin  = np.min(de)
premin = np.min(de_pre)
premax = np.max(de_pre)
# print(de)
print(premax, premin, demax, demin)