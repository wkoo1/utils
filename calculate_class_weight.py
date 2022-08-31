import numpy as np
 
from PIL import Image
 
import os
import math
 
classes = ['background', 'wall', 'floor', 'cabinet', 'bed', 'chair', 'sofa', 'table', 'door',
           'window', 'bookshelf', 'picture', 'counter', 'blinds', 'desk', 'shelves', 'curtain',
           'dresser', 'pillow', 'mirror', 'floor mat', 'clothes', 'ceiling', 'books', 'refridgerator',
           'television', 'paper', 'towel', 'shower curtain', 'box', 'whiteboard', 'person', 'night stand',
           'toilet', 'sink', 'lamp', 'bathtub', 'bag', 'otherstructure', 'otherfurniture', 'otherprop']
 
# 每一类的像素数量
class_count = [0 for i in range(41)]
# 每一类的像素所占比例
class_count_percent = [0 for i in range(41)]
 
root = 'Z:\\x\\dataset\\nyuv2'
txt_fname = ('Z:\\x\\dataset\\nyuv2\\train.txt')
with open(txt_fname, 'r') as f:
    images = f.read().split()
label_list = [os.path.join(root, 'labels40', i + '.png') for i in images]
 
for label_name in label_list:
    label = np.array(Image.open(label_name))
    label = label.flatten()
    for i in label:
        # 遍历label图计算每一类的像素数量
        class_count[int(i)] = class_count[int(i)] + 1
    print(label_name)
 
# 所有像素的总数
all_class_pixel_count = sum(class_count)
 
for i in range(41):
    # 计算每一类的像素所占比例
    class_count_percent[i] = class_count[i] / all_class_pixel_count
 
# 按比例进行排序,找出比例的中位数以及对应类
class_percent_sort = [i for i in class_count_percent]
class_percent_sort.sort()
median = 0
middle_count = 0
middle_class = 0
# for i in range(41):
#     middle_count += class_percent_sort[i]
#     if middle_count > 0.5:
#         median = i
#         break
# median_percent = class_percent_sort[median]
median_percent = class_percent_sort[20]
for i in range(41):
    if median_percent == class_count_percent[i]:
        middle_class = i
 
# 将每个类的比例除以中位数比例得到权重
class_weight = [0 for i in range(41)]
for i in range(41):
    # class_weight[i] = class_count_percent[i] / median_percent
    class_weight[i] = 1 / math.log(class_count[i])
 
weights = [0 for i in range(41)]
for i in range(41):
    weights[i] = 40 * class_weight[i] / sum(class_weight)
 
print(sum(class_count_percent), sum(class_weight))
 
f = open('Z:\\x\\dataset\\nyuv2\\class.txt', 'w')
f.write('all_class_pixel_count is： ' + str(all_class_pixel_count) + '\n')
f.write('median_class is： ' +str(middle_class) + '\n')
f.write('median_percent is： ' +str(median_percent) + '\n')
for i in range(41):
    f.write('class_label: ' + str(i) + '      '
            + 'class_name: ' + classes[i] + '      '
            + 'class_pixels_count: ' + str(class_count[i]) + '      '
            + 'class_pixels_percent: ' + str(class_count_percent[i]) + '      '
            + 'class_weight: ' + str(weights[i]) + '\n')