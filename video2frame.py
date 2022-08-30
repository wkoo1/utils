import cv2
import os
 
#待提取视频的路径
#video_path=r"D:/oukai/crazy/Wakayama_echo_heart/echoimage/20191225/ADD_2CV/201602080009 2CV.avi"
video_path=r"D:/oukai/crazy/gitfile/unetattention-pytorch-new/20160222_2CV_all_noclassweight.mp4"
#生成图片的路径
#img_path=r'D:/oukai/crazy/Wakayama_echo_heart/echoimage/images/ADD_2CV/201602080009/'
img_path=r'D:/oukai/crazy/gitfile/unetattention-pytorch-new/test_comparison/'
#生成img_path文件夹
if not os.path.isdir(img_path):
    os.mkdir(img_path,)

#cv2.VideoCapture可以提取视频的第一帧，返回两个值：
#第一个是bool值，表示有没有提取到；第二个是对应的帧
vidcap = cv2.VideoCapture(video_path)
(cap,frame)= vidcap.read()

if cap==False:
    print('cannot open video file')
count = 0

#将读取的帧对应的图片按顺序重命名为000000.jpg六位整数的格式，并写入img_path路径
#因为相邻帧可能过于相似，可以每隔几帧取一帧，由for循环完成
#while cap and count<100:
while cap:
  cv2.imwrite(os.path.join(img_path,'imageall_noclassweight'+'%.6d.jpg'%count),frame) #201602080009_
  print('image'+'%.6d.jpg'%count)
  count += 1
  for i in range(1):
    (cap,frame)= vidcap.read()