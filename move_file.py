import os
import shutil


#把所有的\\换成/
num=0
rootpath=r"/home/chenj0g/rgb_flow/rgbflow"

for curdir,roots,files in os.walk(rootpath):
    print(curdir)
    num=num+1
N=4
num=(num)/4
num=max(1,num)
print(num)
dirend=['/home/chenj0g/rgb_flow/rgbflow1','/home/chenj0g/rgb_flow/rgbflow2','/home/chenj0g/rgb_flow/rgbflow3','/home/chenj0g/rgb_flow/rgbflow4']#绝对路径 加/home
cnt=-1
flag=0
for curdir,roots,files in os.walk(rootpath):
    if cnt==-1:
        cnt=0
        continue
    if cnt>=num:
        cnt=1
        flag=flag+1
    savename=dirend[flag]+'/'+curdir.split('/')[-1]
    cnt=cnt+1
    print(savename)
    # shutil.move(curdir,savename)

