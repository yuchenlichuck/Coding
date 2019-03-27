# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:21:15 2019

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

    img_save_path=r'G:\2019.3.27'
    file_dir=r'G:\2019.3.27\data\DR'
    i=0
    j=0
    for j in range(0,5):
        for root, dirs, files in os.walk(file_dir):  
            for file in files:
                img_file_path = os.path.join(root,file)
                
                image_save_path=os.path.join(img_save_path,str(int(i/4198)),'DR')
                i=i+1
                print(int(i/4198))
        #    local_img_dir + '\\' +  org_lable[i] +'\\'+ file_name_list[i]
                #img_save_path = save_dir+ '\\'+ org_lable[i] +'\\'+ pred_lable[i]
                mkdir(image_save_path)
                shutil.copy(img_file_path,image_save_path+ '\\' + file)
