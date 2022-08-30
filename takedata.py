from fileinput import filename
import shutil
import os
import glob

# def copy_file(old_path, new_path):
new_path = "D:\\oukai\\dataset\\cityscapes\\gtFine\\test_depth"
#old_path_pure = 'D:\\oukai\\dataset\\cityscapes\\gtFine\\val\\frankfurt'
old_path = 'D:\\oukai\\dataset\\cityscapes\\gtFine\\test\\munich\\**_instanceIds.png'
if not os.path.exists(new_path):
    os.makedirs(new_path)
#filelist = os.listdir(old_path)  # 列出该目录下的所有文件,listdir返回的是文件列表是不包含路径的。
filelist = glob.glob(old_path)
#print(filelist)
#name = total_seg[i][:-4]+'\n'
cout = 0
for file in filelist:
    # filename, extension = os.path.splitext(file)
    filepath, filename = os.path.split(file)
    #if extension == ".png" or extension == ".jpg":
    #if extension == ".json":
    print(filename)
    cout += 1
    src = os.path.join(filepath, filename)
    dst = os.path.join(new_path, filename)
    # print('src:', src)
    # print('dst:', dst)
    shutil.copy(src, dst)

print(cout)
 
 
# if __name__ == '__main__':
#     # remove_file("E:\\数据集\\total", "E:\\Desk\\JPEGImages")
#     copy_file("D:\\oukai\\dataset\\cityscapes\\gtFine\\val", "D:\\oukai\\dataset\\cityscapes\\gtFine\\val_labels")