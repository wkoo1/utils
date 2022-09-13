import os
import shutil

# 查找指定文件夹下所有相同后缀名的文件
def search_file_suffix(dirPath, suffix):
    dirs = os.listdir(dirPath)
    for currentFile in dirs:
        absPath = dirPath + '/' + currentFile
        if os.path.isdir(absPath):
            search_file_suffix(absPath, suffix)
        elif currentFile.split('.')[-1] == suffix: # 文件后缀名相同，则打印该文件的绝对路径
            print(absPath)
            cout = 0
            filepath, filename = os.path.split(absPath)
            print(filename)
            cout += 1
            src = os.path.join(filepath,filename)
            dst = os.path.join(new_path, filename)
            shutil.copy(src, dst)

if __name__ == "__main__":
    dirPath = 'D:/oukai/dataset/Camus/testing'
    suffix = 'raw'
    new_path = "D:/oukai/dataset/Camus/test"
    search_file_suffix(dirPath, suffix)

