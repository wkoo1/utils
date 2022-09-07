import os
import sys

path = r'D:/chrome download/ffmpeg-2022-08-03-git-d3f48e68b3-full_build/bin/image/'

f = os.listdir(path)
 
n = 0

# for i in f:
#     #oldname = path + f[n]
#     oldname = path + f[n]
#     #newname = path + '8.4KP_' + f[n]
#     #newname = path + '39.0KP_' + str(n) + '.json'
#     newname = path + '4cv20160222_' + f[n]
#     os.rename(oldname,newname)
#     print(oldname, '====>' ,newname)
#     n += 1
    
i=1
#对目录下的文件进行遍历
for file in os.listdir(path):
#判断是否是文件
    if os.path.isfile(os.path.join(path,file))==True:
#设置新文件名
        new_name=file.replace(file,"%d.png"%i)
#重命名
        os.rename(os.path.join(path,file),os.path.join(path,new_name))
        i+=1
#结束
print ("End")