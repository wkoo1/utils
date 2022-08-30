import os
import sys

path = r'D:/oukai/crazy/Wakayama_echo_heart/echoimage/images/20160222/4CV/'

f = os.listdir(path)
 
n = 0

for i in f:
    #oldname = path + f[n]
    oldname = path + f[n]
    #newname = path + '8.4KP_' + f[n]
    #newname = path + '39.0KP_' + str(n) + '.json'
    newname = path + '4cv20160222_' + f[n]
    os.rename(oldname,newname)
    print(oldname, '====>' ,newname)
    n += 1
    