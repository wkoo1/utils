# coding=utf-8
import cv2
import os

import cv2 as cv
cap = cv.VideoCapture('20160115_2CV.avi')
fourcc = cv.VideoWriter_fourcc(*'MP42') 
"""
cv2.VideoWriter_fourcc(‘P’,‘I’,‘M’,‘1’) = MPEG-1 codec 
cv2.VideoWriter_fourcc(‘M’,‘J’,‘P’,‘G’) = motion-jpeg codec --> mp4v 
cv2.VideoWriter_fourcc(‘M’, ‘P’, ‘4’, ‘2’) = MPEG-4.2 codec 可以插入ppt播放
cv2.VideoWriter_fourcc(‘D’, ‘I’, ‘V’, ‘3’) = MPEG-4.3 codec 
cv2.VideoWriter_fourcc(‘D’, ‘I’, ‘V’, ‘X’) = MPEG-4 codec --> avi 
cv2.VideoWriter_fourcc(‘U’, ‘2’, ‘6’, ‘3’) = H263 codec 
cv2.VideoWriter_fourcc(‘I’, ‘2’, ‘6’, ‘3’) = H263I codec 
cv2.VideoWriter_fourcc(‘F’, ‘L’, ‘V’, ‘1’) = FLV1 codec
"""
width, height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv.VideoWriter('0115.mp4', fourcc, 20.0, (width,  height))
while cap.isOpened():
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        break
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
out.release()
cv.destroyAllWindows()