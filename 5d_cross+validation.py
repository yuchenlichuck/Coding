# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:21:15 2019

@author: PC
"""

import os
import shutil

file_path=r'G:\3.27\data\'

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
    
    
