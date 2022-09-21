with open('D:/oukai/crazy/utils/result.txt','r') as r:
    lines=r.readlines()
with open('D:/oukai/crazy/utils/result_output.txt','w') as w:
    for l in lines:
       if 'dice:' in l:
          w.write(l)