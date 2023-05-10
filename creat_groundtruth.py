import os
import cv2
import colorsys
import numpy as np
from tqdm import tqdm

class MaskVisualizer:
    def __init__(self, num_classes=19+1):
        self.num_classes = num_classes
        if self.num_classes <= 21:
            self.colors = [ (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128), (128, 0, 128), (0, 128, 128), 
                            (128, 128, 128), (64, 0, 0), (192, 0, 0), (64, 128, 0), (192, 128, 0), (64, 0, 128), (192, 0, 128), 
                            (64, 128, 128), (192, 128, 128), (0, 64, 0), (128, 64, 0), (0, 192, 0), (128, 192, 0), (0, 64, 128), 
                            (128, 64, 12)]
        else:
            hsv_tuples = [(x / self.num_classes, 1., 1.) for x in range(self.num_classes)]
            self.colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
            self.colors = list(map(lambda x: (int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)), self.colors))
        # self.class_names = ['class_' + str(i) for i in range(num_classes)]
        self.class_names     = ["road","sidewalk", "building", "wall", "fence", "pole", "traffic light", "traffic sign", "vegetation", "terrain", "sky", "person", 'rider', 'car', 'truck', 'bus', 'train', 'motorcycle', 'bicycle',"ignore"]
        # self.class_names = ['wall', 'floor', 'cabinet', 'bed', 'chair', 'sofa', 'table', 'door', 'window', 'bookshelf', 'picture', 'counter', 'blinds', 'desk', 'shelves', 'curtain', 'dresser', 'pillow', 'mirror', 'floor mat', 'clothes', 'ceiling', 'books', 'refridgerator', 'television', 'paper', 'towel', 'shower curtain', 'box', 'whiteboard', 'person', 'night stand', 'toilet', 'sink', 'lamp', 'bathtub', 'bag', 'otherstructure', 'otherfurniture', 'otherprop',"ignore"]
    def visualize(self, image_folder, mask_folder, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        for filename in tqdm(os.listdir(image_folder)):
            # 检查文件名是否以指定后缀结尾
            if filename.endswith('.jpg'):
                # 读取图像
                image = cv2.imread(os.path.join(image_folder, filename))
                print(filename)
                # 获取掩码文件名
            #cityscapes dataset
            prefix_len1 = len('frankfurt_000000_000294')  # 设置前缀的长度
            prefix_len2 = len('lindau_000000_000019')  # 设置前缀的长度
            prefix_len3 = len('munster_000031_000019')  # 设置前缀的长度
            for name in os.listdir(mask_folder):
                if name[:prefix_len1] == filename[:prefix_len1] or name[:prefix_len2] == filename[:prefix_len2] or name[:prefix_len3] == filename[:prefix_len3]:
                    mask_filename = name
                    break
            #nyuv2 dataset
            # mask_filename = os.path.splitext(filename)[0] + '.png'
            # print(mask_filename)
            # 检查掩码文件是否存在
            if os.path.exists(os.path.join(mask_folder, mask_filename)):
                # 读取掩码图像
                mask = cv2.imread(os.path.join(mask_folder, mask_filename), cv2.IMREAD_GRAYSCALE)
                # print(mask.shape)
                # 获取掩码图像中出现的所有类别
                classes = np.unique(mask)
                # print(classes)
                # 如果掩码中有类别
                if len(classes) > 0:
                    # 将掩码图像进行染色
                    color_mask = np.zeros_like(image)
                    for i in range(len(self.class_names)):
                        if i in classes:
                            color_mask[mask == i] = self.colors[i][::-1]
                    # 将染色后的掩码图像与原始图像进行融合
                    alpha = 0.3
                    blended = cv2.addWeighted(image, alpha, color_mask, 1 - alpha, 0)
                    # 保存融合后的图像
                    output_filename = os.path.join(output_folder, filename)
                    cv2.imwrite(output_filename, blended)
                else:
                    print('Mask file not found for image {}.'.format(filename))
        print('Done.')

if __name__ == '__main__':
    image_folder = 'Z:/x/dataset/cityscapes/leftImg8bit/val_jpg'
    mask_folder = 'Z:/x/dataset/cityscapes/gtFine/val_labels19_nobackground'
    output_folder = 'Z:/x/dataset/cityscapes/colorgroundtruth'
    # image_folder = 'Z:/x/dataset/nyuv2/images'
    # mask_folder = 'Z:/x/dataset/nyuv2/labels40'
    # output_folder = 'Z:/x/dataset/nyuv2/colorgroundtruth'
    visualizer = MaskVisualizer()
    visualizer.visualize(image_folder, mask_folder, output_folder)