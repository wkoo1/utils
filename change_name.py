import os
import sys

path = r'D:/oukai\dataset/Camus/train_labels_ES_png/'

f = os.listdir(path)
 
n = 0

for i in f:
    #oldname = path + f[n]
    oldname = path + f[n]
    #newname = path + '8.4KP_' + f[n]
    #newname = path + '39.0KP_' + str(n) + '.json'
    newname = path + f[n][:-7] + '.png'
    #print(newname)
    os.rename(oldname,newname)
    print(oldname, '====>' ,newname)
    n += 1
print(n)
# i=1
# #对目录下的文件进行遍历
# for file in os.listdir(path):
# #判断是否是文件
#     if os.path.isfile(os.path.join(path,file))==True:
# #设置新文件名
#         new_name=file.replace(file,"%d.png"%i)
# #重命名
#         os.rename(os.path.join(path,file),os.path.join(path,new_name))
#         i+=1
# #结束
# print ("End")