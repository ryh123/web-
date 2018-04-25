from PIL import Image
from PIL import ImageChops
import os
from pathlib import Path

def compare_images(path_one, path_two, diff_save_location):
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    diff = ImageChops.difference(image_one, image_two)
    if diff.getbbox() is None:
        print("ok")
    else:
        diff.save(diff_save_location)
        print("save")
 
if __name__ == '__main__':
    diffpath='D:\\Exdiff'
    if Path(diffpath).is_dir():
        pass
    else:
        Path(diffpath).mkdir()
    f = open(r'I:\python test\网站状态监控\web监控项目\urls.txt','r')                                   #将url目录的路径填入
    urllist = f.readlines()
    for url in urllist:
        url=url.replace('http://','')
        url=url.strip('\n')
        url=url.replace('#tips','')
        url=url.strip('/')
        path_one='D:\\Exnow'+'\\'+url+'.png'
        path_two='D:\\Exstandard'+'\\'+url+'.png'
        path_diff=diffpath+"\\"+url+'.png'
        if os.path.exists(path_one) and os.path.exists(path_two):		
            compare_images(path_one,path_two,path_diff)
        else:
            continue