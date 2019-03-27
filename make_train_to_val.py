# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:12:20 2019

@author: PC
"""
import os
import shutil

def mkdir(path):
    '''
    创建不存在的文件夹
    '''
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
         # 创建目录操作函数
        os.makedirs(path)
        # print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(path + ' 目录已存在')
        return False
    
if __name__ == '__main__':
    
    
    file_dir=r'G:\2019.3.27\set1'

    dirs = os.listdir(file_dir)
    i=0
    j=0
    for dir in dirs:
        img_file_path = os.path.join(file_dir,dir)
        
        
        i=i+1
        print(i)
        for root, dirs, files in os.walk(img_file_path):  
            if os.path.basename(root)=='test':
                continue
            print(os.path.basename(root))
            if 'test' in root:
                continue
            j=0
            length=len(files)
            print(length)
            for file in files:

                img_file_path = os.path.join(root,file)
               # image_save_path=os.path.join(img_save_path,str(int(i/4198)),'DR')
          #      i=i+1
              #  print(int(i/4198))
        #    local_img_dir + '\\' +  org_lable[i] +'\\'+ file_name_list[i]
                #img_save_path = save_dir+ '\\'+ org_lable[i] +'\\'+ pred_lable[i]
                save=file_dir+'\\'+ dir + '\\' + 'val'+'\\'+os.path.basename(root)
                mkdir(save)
                shutil.move(img_file_path,save+'\\'+file)
                j=j+1;
                if j>(int)(0.05*length):
                    break
                
                
                
                
                
